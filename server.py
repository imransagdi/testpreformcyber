
import json
import os
import random
import secrets
import socket
import sqlite3
import time
import uuid

from dotenv import load_dotenv

load_dotenv()

try:
    import psycopg
    from psycopg.rows import dict_row
except ImportError:
    psycopg = None
    dict_row = None

from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from gui import PAGE
from main import CyberGame, RANKS
from update import PlayerEconomy
from timer import GameTimer
from loguser import build_log_page


app = Flask(__name__)
rooms = {}

DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()
DB_PATH = os.environ.get("CYBERNET_DB", "cybernet.db")

print("================================")
print("CYBER//NET DATABASE CHECK")
print("DATABASE_URL configured:", bool(DATABASE_URL))
print("PSYCOPG installed:", psycopg is not None)
print("DATABASE BACKEND:", "NEON" if DATABASE_URL else "SQLITE")
print("================================")

ALLOWED_GAME_TIMES = [5, 10, 15, 30, 60]
PROGRESS_SAVE_INTERVAL = 15

GPU_PRICE = 250
GPU_INCOME_PER_SECOND = 10
GPU_ELECTRICITY_PER_SECOND = 2

ANALYZE_COOLDOWN = 10
ANALYSIS_MIN_TIME = 5.0
ANALYSIS_MAX_TIME = 7.0
LOCK_DEFENSE_TIME = 30.0
LOCK_MIN_TIME = 1.0
LOCK_MAX_TIME = 3.0

JUMPSCARE_CHANCE = 0.25
JUMPSCARE_MIN_DELAY = 10
JUMPSCARE_COOLDOWN = 60


# =========================================================
# DATABASE / ACCOUNTS
# =========================================================

def db_connect():
    """Connect to Neon when DATABASE_URL is set; otherwise use local SQLite."""
    if DATABASE_URL:
        if psycopg is None:
            raise RuntimeError(
                "DATABASE_URL is set, but psycopg is not installed. "
                "Install the project requirements."
            )
        return psycopg.connect(DATABASE_URL, row_factory=dict_row)

    connection = sqlite3.connect(DB_PATH, timeout=10)
    connection.row_factory = sqlite3.Row
    return connection


def db_execute(db, query, params=()):
    """Run SQL with placeholders compatible with both SQLite and PostgreSQL."""
    if DATABASE_URL:
        query = query.replace("?", "%s")
    return db.execute(query, params)


def init_database():
    with db_connect() as db:
        if DATABASE_URL:
            db_execute(db, """
                CREATE TABLE IF NOT EXISTS accounts (
                    id BIGSERIAL PRIMARY KEY,
                    username TEXT NOT NULL,
                    password_hash TEXT NOT NULL,
                    progress TEXT NOT NULL DEFAULT '{}',
                    created_at DOUBLE PRECISION NOT NULL
                )
            """)
            db_execute(db, """
                CREATE UNIQUE INDEX IF NOT EXISTS accounts_username_lower_idx
                ON accounts (LOWER(username))
            """)
        else:
            db_execute(db, """
                CREATE TABLE IF NOT EXISTS accounts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE COLLATE NOCASE,
                    password_hash TEXT NOT NULL,
                    progress TEXT NOT NULL DEFAULT '{}',
                    created_at REAL NOT NULL
                )
            """)


init_database()


HARDWARE_PARTS = {
    "cpu": {"level_attr": "cpu_level", "base_price": 250, "name": "CPU"},
    "ram": {"level_attr": "ram_level", "base_price": 400, "name": "RAM"},
    "storage": {"level_attr": "storage_level", "base_price": 300, "name": "STORAGE"},
}

HARDWARE_SLOT_TYPES = {
    "cpu": "cpu",
    "ram": "ram",
    "storage": "storage",
    "gpu1": "gpu",
    "gpu2": "gpu",
    "gpu3": "gpu",
    "gpu4": "gpu",
}


def make_hardware_component(part_type, tier=1, component_id=None):
    names = {
        "cpu": "CPU",
        "ram": "RAM",
        "storage": "STORAGE",
        "gpu": "GPU",
    }

    tier = max(1, int(tier))

    return {
        "id": str(component_id or uuid.uuid4().hex[:12]),
        "type": part_type,
        "tier": tier,
        "name": f"{names.get(part_type, part_type.upper())} T{tier}",
    }


def normalize_hardware(player, migrate_legacy=False):
    """Ensure motherboard slots and spare component inventory are valid."""
    slots = getattr(player, "hardware_slots", None)

    if not isinstance(slots, dict):
        slots = {}

    if migrate_legacy or not slots:
        slots = {
            "cpu": make_hardware_component(
                "cpu", getattr(player, "cpu_level", 1), "factory-cpu"
            ),
            "ram": make_hardware_component(
                "ram", getattr(player, "ram_level", 1), "factory-ram"
            ),
            "storage": make_hardware_component(
                "storage", getattr(player, "storage_level", 1), "factory-storage"
            ),
            "gpu1": None,
            "gpu2": None,
            "gpu3": None,
            "gpu4": None,
        }

        legacy_gpu_count = max(0, int(getattr(player, "gpu_count", 0)))

        for index in range(min(4, legacy_gpu_count)):
            slots[f"gpu{index + 1}"] = make_hardware_component(
                "gpu", 1, f"legacy-gpu-{index + 1}"
            )

        inventory = getattr(player, "hardware_inventory", [])

        if not isinstance(inventory, list):
            inventory = []

        for index in range(max(0, legacy_gpu_count - 4)):
            inventory.append(make_hardware_component("gpu", 1))

        player.hardware_inventory = inventory

    else:
        for slot_key, part_type in (
            ("cpu", "cpu"),
            ("ram", "ram"),
            ("storage", "storage"),
        ):
            current = slots.get(slot_key)

            if not isinstance(current, dict) or current.get("type") != part_type:
                level_attr = HARDWARE_PARTS[part_type]["level_attr"]
                slots[slot_key] = make_hardware_component(
                    part_type,
                    getattr(player, level_attr, 1),
                )

        for index in range(1, 5):
            slot_key = f"gpu{index}"
            current = slots.get(slot_key)

            if not isinstance(current, dict) or current.get("type") != "gpu":
                slots[slot_key] = None

    inventory = getattr(player, "hardware_inventory", [])

    if not isinstance(inventory, list):
        inventory = []

    clean_inventory = []

    for item in inventory:
        if not isinstance(item, dict):
            continue

        if item.get("type") not in ("cpu", "ram", "storage", "gpu"):
            continue

        try:
            clean_inventory.append(
                make_hardware_component(
                    item["type"],
                    item.get("tier", 1),
                    item.get("id"),
                )
            )
        except (TypeError, ValueError):
            continue

    player.hardware_slots = slots
    player.hardware_inventory = clean_inventory

    sync_hardware_stats(player)

    return slots, clean_inventory


def sync_hardware_stats(player):
    slots = getattr(player, "hardware_slots", {})

    for slot_key, level_attr in (
        ("cpu", "cpu_level"),
        ("ram", "ram_level"),
        ("storage", "storage_level"),
    ):
        part = slots.get(slot_key) if isinstance(slots, dict) else None

        if isinstance(part, dict):
            setattr(
                player,
                level_attr,
                max(1, int(part.get("tier", 1))),
            )

    gpu_count = 0

    if isinstance(slots, dict):
        for index in range(1, 5):
            part = slots.get(f"gpu{index}")

            if isinstance(part, dict) and part.get("type") == "gpu":
                gpu_count += 1

    player.gpu_count = gpu_count

    player.speed_multiplier = (
        1
        + max(0, int(getattr(player, "speed_upgrade_level", 0))) * 0.25
        + max(0, int(getattr(player, "cpu_level", 1)) - 1) * 0.15
    )


def hardware_payload(player):
    slots, inventory = normalize_hardware(player)

    return {
        "cpu_level": getattr(player, "cpu_level", 1),
        "ram_level": getattr(player, "ram_level", 1),
        "gpus": getattr(player, "gpu_count", 0),
        "storage_level": getattr(player, "storage_level", 1),
        "slots": slots,
        "inventory": inventory,
    }


def save_player_progress(player, force=True):
    """
    Save player progress.

    Important actions save immediately.
    Passive background updates are throttled to once every 15 seconds.
    """
    normalize_hardware(player)

    account_id = getattr(player, "account_id", None)

    if not account_id:
        return

    now = time.time()
    last_save = getattr(player, "_last_progress_save_at", 0)

    if not force and now - last_save < PROGRESS_SAVE_INTERVAL:
        return

    progress = {
        "coins": player.economy.coins,
        "exploit_level": player.economy.exploit_level,
        "firewall_level": player.economy.firewall_level,
        "inventory": list(player.economy.inventory),
        "reputation": getattr(player, "reputation", 0),
        "hacks_done": getattr(player, "hacks_done", 0),
        "speed_upgrade_level": getattr(player, "speed_upgrade_level", 0),
        "firewall_upgrade_level": getattr(player, "firewall_upgrade_level", 0),
        "exploit_upgrade_level": getattr(player, "exploit_upgrade_level", 0),
        "gpu_count": getattr(player, "gpu_count", 0),
        "ddos_owned": bool(getattr(player, "ddos_owned", False)),
        "mitm_owned": bool(getattr(player, "mitm_owned", False)),
        "cpu_level": getattr(player, "cpu_level", 1),
        "ram_level": getattr(player, "ram_level", 1),
        "storage_level": getattr(player, "storage_level", 1),
        "hardware_slots": getattr(player, "hardware_slots", {}),
        "hardware_inventory": getattr(player, "hardware_inventory", []),
    }

    with db_connect() as db:
        db_execute(
            db,
            "UPDATE accounts SET progress = ? WHERE id = ?",
            (json.dumps(progress), account_id),
        )

    player._last_progress_save_at = now


def load_player_progress(player, account_id):
    with db_connect() as db:
        row = db_execute(
            db,
            "SELECT progress FROM accounts WHERE id = ?",
            (account_id,),
        ).fetchone()

    if not row:
        return

    try:
        progress = json.loads(row["progress"])
    except (TypeError, ValueError):
        return

    player.account_id = account_id
    player.economy.coins = max(0, int(progress.get("coins", 500)))

    player.economy.exploit_level = max(
        1, int(progress.get("exploit_level", 1))
    )

    player.economy.firewall_level = max(
        1, int(progress.get("firewall_level", 1))
    )

    inventory = progress.get("inventory", [])

    if isinstance(inventory, list):
        player.economy.inventory = [
            str(item).lower()
            for item in inventory
            if isinstance(item, str)
        ]

    player.ddos_owned = bool(progress.get("ddos_owned", False))
    player.mitm_owned = bool(progress.get("mitm_owned", False))

    player.cpu_level = max(1, int(progress.get("cpu_level", 1)))
    player.ram_level = max(1, int(progress.get("ram_level", 1)))
    player.storage_level = max(1, int(progress.get("storage_level", 1)))

    player.reputation = max(0, int(progress.get("reputation", 0)))
    player.hacks_done = max(0, int(progress.get("hacks_done", 0)))

    player.speed_upgrade_level = max(
        0, int(progress.get("speed_upgrade_level", 0))
    )

    player.firewall_upgrade_level = max(
        0, int(progress.get("firewall_upgrade_level", 0))
    )

    player.exploit_upgrade_level = max(
        0, int(progress.get("exploit_upgrade_level", 0))
    )

    player.gpu_count = max(0, int(progress.get("gpu_count", 0)))

    saved_inventory = progress.get("hardware_inventory", [])

    player.hardware_inventory = (
        saved_inventory if isinstance(saved_inventory, list) else []
    )

    saved_slots = progress.get("hardware_slots")

    if isinstance(saved_slots, dict):
        player.hardware_slots = saved_slots
        normalize_hardware(player)
    else:
        player.hardware_slots = {}
        normalize_hardware(player, migrate_legacy=True)

    player._last_progress_save_at = time.time()


def account_for_request():
    """Validate a bearer token for account-aware requests."""
    token = request.headers.get("X-Cybernet-Token", "")

    if not token:
        data = request.get_json(silent=True) or {}
        token = str(data.get("token", ""))

    if not token:
        return None

    account_id = account_sessions.get(token)

    if not account_id:
        return None

    with db_connect() as db:
        return db_execute(
            db,
            "SELECT id, username FROM accounts WHERE id = ?",
            (account_id,),
        ).fetchone()


account_sessions = {}


def register_account(username, password):
    username = str(username or "").strip()

    if not 3 <= len(username) <= 24:
        return None, "Username must be 3–24 characters."

    if not all(c.isalnum() or c in "_-" for c in username):
        return None, "Username can only use letters, numbers, _ and -."

    if not isinstance(password, str) or len(password) < 8:
        return None, "Password must be at least 8 characters."

    password_hash = generate_password_hash(password)

    try:
        with db_connect() as db:
            if DATABASE_URL:
                row = db_execute(
                    db,
                    """
                    INSERT INTO accounts (username, password_hash, progress, created_at)
                    VALUES (?, ?, '{}', ?)
                    RETURNING id
                    """,
                    (username, password_hash, time.time()),
                ).fetchone()

                account_id = row["id"]

            else:
                cursor = db_execute(
                    db,
                    """
                    INSERT INTO accounts (username, password_hash, progress, created_at)
                    VALUES (?, ?, '{}', ?)
                    """,
                    (username, password_hash, time.time()),
                )

                account_id = cursor.lastrowid

        return account_id, None

    except Exception as exc:
        if isinstance(exc, sqlite3.IntegrityError) or (
            psycopg is not None and isinstance(exc, psycopg.IntegrityError)
        ):
            return None, "That username is already taken."

        raise


def authenticate_account(username, password):
    with db_connect() as db:
        row = db_execute(
            db,
            """
            SELECT id, username, password_hash
            FROM accounts
            WHERE LOWER(username) = LOWER(?)
            """,
            (str(username or "").strip(),),
        ).fetchone()

    if not row or not check_password_hash(
        row["password_hash"],
        str(password or ""),
    ):
        return None

    return row


@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json(silent=True) or {}

    account_id, error = register_account(
        data.get("username"),
        data.get("password"),
    )

    if error:
        return jsonify({"success": False, "error": error}), 400

    token = secrets.token_urlsafe(32)
    account_sessions[token] = account_id

    return jsonify({
        "success": True,
        "token": token,
        "account_id": account_id,
        "message": "Account created. Log in to continue.",
    })


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}

    account = authenticate_account(
        data.get("username"),
        data.get("password"),
    )

    if not account:
        return jsonify({
            "success": False,
            "error": "Invalid username or password.",
        }), 401

    token = secrets.token_urlsafe(32)
    account_sessions[token] = account["id"]

    return jsonify({
        "success": True,
        "token": token,
        "account_id": account["id"],
        "username": account["username"],
    })


@app.route("/api/logout", methods=["POST"])
def logout():
    data = request.get_json(silent=True) or {}

    token = request.headers.get(
        "X-Cybernet-Token",
        data.get("token", ""),
    )

    account_sessions.pop(str(token), None)

    return jsonify({"success": True})


# =========================================================
# PLAYER PROFILE + SESSION OWNERSHIP
# =========================================================

def request_token():
    token = request.headers.get("X-Cybernet-Token", "")

    if not token:
        data = request.get_json(silent=True) or {}
        token = str(data.get("token", ""))

    return token


def session_expired_response():
    return jsonify({
        "success": False,
        "error": "SESSION EXPIRED. PLEASE LOG IN AGAIN.",
    }), 401


def _clean_int(value, default=0, minimum=0):
    try:
        return max(minimum, int(value))
    except (TypeError, ValueError):
        return max(minimum, default)


def rank_for_reputation(reputation):
    rank = RANKS[0][1]

    for threshold, name in RANKS:
        if reputation >= threshold:
            rank = name

    return rank


def build_profile(username, progress, source):
    if not isinstance(progress, dict):
        progress = {}

    slots = progress.get("hardware_slots")
    slots = slots if isinstance(slots, dict) else None

    def tier(slot_key, fallback_key):
        part = slots.get(slot_key) if slots else None

        if isinstance(part, dict):
            return _clean_int(part.get("tier", 1), 1, 1)

        return _clean_int(progress.get(fallback_key, 1), 1, 1)

    if slots is not None:
        gpus = sum(
            1
            for index in range(1, 5)
            if isinstance(slots.get(f"gpu{index}"), dict)
            and slots[f"gpu{index}"].get("type") == "gpu"
        )
    else:
        gpus = min(4, _clean_int(progress.get("gpu_count", 0)))

    reputation = _clean_int(progress.get("reputation", 0))

    return {
        "username": str(username),
        "reputation": reputation,
        "rank": rank_for_reputation(reputation),
        "coins": _clean_int(
            progress.get("coins", PlayerEconomy.STARTING_COINS)
        ),
        "hacks_done": _clean_int(progress.get("hacks_done", 0)),
        "hardware": {
            "cpu_tier": tier("cpu", "cpu_level"),
            "ram_tier": tier("ram", "ram_level"),
            "gpus": gpus,
            "storage_tier": tier("storage", "storage_level"),
        },
        "source": source,
    }


@app.route("/api/profile", methods=["GET"])
def player_profile():
    account = account_for_request()

    if not account:
        return session_expired_response()

    with db_connect() as db:
        row = db_execute(
            db,
            "SELECT username, progress FROM accounts WHERE id = ?",
            (account["id"],),
        ).fetchone()

    if not row:
        return session_expired_response()

    try:
        saved = json.loads(row["progress"])
    except (TypeError, ValueError):
        saved = {}

    profile = build_profile(row["username"], saved, "database")

    room = rooms.get(str(request.args.get("room", "")).strip())
    player_id = str(request.args.get("player", "")).strip()

    if room and player_id:
        player = get_player(room["game"], player_id)

        if player and str(getattr(player, "account_id", "")) == str(account["id"]):
            update_bitcoin_farm(player)
            normalize_hardware(player)

            live = {
                "coins": player.economy.coins,
                "reputation": getattr(player, "reputation", 0),
                "hacks_done": getattr(player, "hacks_done", 0),
                "hardware_slots": getattr(player, "hardware_slots", {}),
                "cpu_level": getattr(player, "cpu_level", 1),
                "ram_level": getattr(player, "ram_level", 1),
                "storage_level": getattr(player, "storage_level", 1),
                "gpu_count": getattr(player, "gpu_count", 0),
            }

            profile = build_profile(row["username"], live, "live")

    response = jsonify({
        "success": True,
        "profile": profile,
    })

    response.headers["Cache-Control"] = "no-store"

    return response


PLAYER_ACTION_ROUTES = {
    "/api/command",
    "/api/buy-gpu",
    "/api/hardware/purchase",
    "/api/hardware/install",
}


@app.before_request
def protect_player_sessions():
    if request.method != "POST" or request.path not in PLAYER_ACTION_ROUTES:
        return None

    data = request.get_json(silent=True) or {}

    room = rooms.get(str(data.get("room", "")).strip())

    if not room:
        return None

    player = get_player(
        room["game"],
        str(data.get("player", "")).strip(),
    )

    owner_id = getattr(player, "account_id", None) if player else None

    if not owner_id:
        return None

    account = account_for_request()

    if not account:
        message = "SESSION EXPIRED. PLEASE LOG IN AGAIN."

        return jsonify({
            "success": False,
            "error": message,
            "output": "ERROR: " + message,
        }), 401

    if str(account["id"]) != str(owner_id):
        message = "THIS SESSION IS NOT AUTHORIZED FOR THAT PLAYER."

        return jsonify({
            "success": False,
            "error": message,
            "output": "ERROR: " + message,
        }), 403

    return None


# =========================================================
# GENERAL HELPERS
# =========================================================

def get_local_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
        sock.close()
        return local_ip

    except Exception:
        return "YOUR-PC-IP"


def get_gpu_price(player):
    return GPU_PRICE


def setup_bitcoin_farm(player):
    if not hasattr(player, "gpu_count"):
        player.gpu_count = 0

    if not hasattr(player, "farm_last_update"):
        player.farm_last_update = time.time()

    if not hasattr(player, "farm_running"):
        player.farm_running = False


def update_bitcoin_farm(player):
    if not player:
        return

    setup_bitcoin_farm(player)

    now = time.time()
    last_update = getattr(player, "farm_last_update", now)
    elapsed = max(0, now - last_update)
    seconds = int(elapsed)

    if seconds <= 0:
        return

    player.farm_last_update = last_update + seconds

    gpu_count = max(0, int(getattr(player, "gpu_count", 0)))

    if gpu_count <= 0:
        player.farm_running = False
        player.farm_last_update = now
        return

    electricity_cost = gpu_count * GPU_ELECTRICITY_PER_SECOND * seconds
    income = gpu_count * GPU_INCOME_PER_SECOND * seconds

    if player.economy.coins < electricity_cost:
        player.farm_running = False
        return

    player.economy.coins -= electricity_cost
    player.economy.coins += income
    player.farm_running = True


def bitcoin_farm_data(player):
    if not player:
        return {
            "gpus": 0,
            "income_per_second": 0,
            "electricity_per_second": 0,
            "net_profit_per_second": 0,
            "running": False,
            "gpu_price": GPU_PRICE,
        }

    setup_bitcoin_farm(player)

    count = max(0, int(player.gpu_count))
    income = count * GPU_INCOME_PER_SECOND
    electricity = count * GPU_ELECTRICITY_PER_SECOND

    return {
        "gpus": count,
        "income_per_second": income,
        "electricity_per_second": electricity,
        "net_profit_per_second": income - electricity,
        "running": bool(player.farm_running),
        "gpu_price": get_gpu_price(player),
    }


def update_all_bitcoin_farms(room):
    if not room or not room.get("game"):
        return

    for player in room["game"].players.values():
        update_bitcoin_farm(player)

        # Passive farm progress does not need a database write every poll.
        save_player_progress(player, force=False)


def add_activity(room, player, action, details=""):
    if not room or not player:
        return

    room.setdefault("activity", []).append({
        "id": str(uuid.uuid4()),
        "time": time.time(),
        "player_id": player.player_id,
        "player_name": player.name,
        "action": str(action).upper(),
        "details": str(details),
    })

    room["activity"] = room["activity"][-200:]


def add_event(room, event_type, **data):
    event = {
        "id": str(uuid.uuid4()),
        "type": event_type,
        "time": time.time(),
        **data,
    }

    room.setdefault("events", []).append(event)
    room["events"] = room["events"][-50:]

    return event


def get_player(game, player_id):
    return game.players.get(str(player_id))


def player_data(player):
    if not player:
        return None

    update_bitcoin_farm(player)

    cooldown_until = getattr(player, "analyze_cooldown_until", 0)

    return {
        "player_id": player.player_id,
        "name": player.name,
        "ip": player.ip,
        "coins": player.economy.coins,
        "exploit_level": player.economy.exploit_level,
        "firewall": player.economy.firewall_level,
        "current_ip": player.current_ip,
        "detection": player.detection,
        "hacks_done": getattr(player, "hacks_done", 0),
        "reputation": getattr(player, "reputation", 0),
        "rank": (
            player.get_rank()
            if hasattr(player, "get_rank")
            else "SCRIPT KIDDIE"
        ),
        "analyze_cooldown": max(
            0,
            round(cooldown_until - time.time(), 1),
        ),
        "bitcoin_farm": bitcoin_farm_data(player),
        "store_items": {
            "ddos": {
                "price": 2500,
                "owned": bool(getattr(player, "ddos_owned", False)),
            },
            "mitm": {
                "price": 2500,
                "owned": bool(getattr(player, "mitm_owned", False)),
            },
        },
        "hardware": hardware_payload(player),
        "team": team_payload(player),
    }


def team_payload(player):
    team = getattr(player, "team", None)

    if team is None:
        return None

    sub = team.sub

    return {
        "name": team.name,
        "type": team.team_type,
        "max_members": team.max_members,
        "members": [member.name for member in team.members],
        "leader": team.leader is player,
        "has_sub": sub is not None,
        "sub_name": sub.name if sub else None,
        "sub_ip": sub.ip if sub else None,
        "firewall": team.firewall_level() if sub else None,
        "shield_active": team.shield_active(),
        "breach_remaining": round(team.breach_remaining(), 1),
    }


def public_teams(game):
    return [
        {
            "name": team.name,
            "type": team.team_type,
            "size": len(team.members),
            "max_members": team.max_members,
            "sub_name": team.sub.name if team.sub else None,
            "sub_ip": team.sub.ip if team.sub else None,
            "breached": bool(team.sub) and not team.shield_active(),
        }
        for team in game.teams.values()
    ]


def generate_room_code():
    while True:
        code = str(random.randint(100000, 999999))

        if code not in rooms:
            return code


def cleanup_game_timer(room):
    if not room.get("started") or room.get("game_over"):
        return bool(room.get("game_over"))

    ends_at = room.get("game_ends_at")

    if ends_at and time.time() >= ends_at:
        room["game_over"] = True

        add_event(
            room,
            "game_over",
            message="GAME TIME EXPIRED.",
        )

        for player in room["game"].players.values():
            save_player_progress(player)

        return True

    return False


def get_leaderboard(room):
    # Farm updates happen in the state update pass, not again here.
    players = sorted(
        room["game"].players.values(),
        key=lambda p: (
            p.economy.coins,
            getattr(p, "hacks_done", 0),
        ),
        reverse=True,
    )

    return [
        {
            "place": place,
            "player_id": player.player_id,
            "name": player.name,
            "coins": player.economy.coins,
            "hacks": getattr(player, "hacks_done", 0),
            "rank": (
                player.get_rank()
                if hasattr(player, "get_rank")
                else "SCRIPT KIDDIE"
            ),
        }
        for place, player in enumerate(players, start=1)
    ]


# =========================================================
# ANALYSIS / LOCK SYSTEM
# =========================================================

DEFENSE_COMMANDS = ["lock"]


def get_active_analysis_for_player(room, player_id):
    for session_id, session in list(room["analysis"].items()):
        if session.get("finished"):
            continue

        if session["attacker"] == player_id:
            return session_id, session, "attacker"

        if session["victim"] == player_id:
            return session_id, session, "victim"

    return None, None, None


def analysis_state(room, player_id):
    session_id, session, role = get_active_analysis_for_player(
        room,
        player_id,
    )

    if not session:
        return None

    remaining = round(
        max(0.0, session["timer"].remaining()),
        1,
    )

    lock_timer = session.get("lock_completion_timer")

    lock_remaining = (
        round(max(0.0, lock_timer.remaining()), 1)
        if lock_timer
        else 0.0
    )

    if role == "victim":
        attacker_id = None
        attacker_name = "UNKNOWN"
    else:
        attacker_id = session["attacker"]
        attacker_name = session["attacker_name"]

    return {
        "role": role,
        "active": True,
        "remaining": remaining,
        "duration": session.get("duration", ANALYSIS_MAX_TIME),
        "lock_remaining": lock_remaining,
        "lock_active": bool(session.get("lock_started", False)),
        "lock_duration": session.get("lock_duration"),
        "victim": session["victim"],
        "victim_name": session["victim_name"],
        "attacker": attacker_id,
        "attacker_name": attacker_name,
        "defense_progress": session["defense_progress"],
        "required_defense": DEFENSE_COMMANDS,
        "lock_defense_time": LOCK_DEFENSE_TIME,
        "lock_min_time": LOCK_MIN_TIME,
        "lock_max_time": LOCK_MAX_TIME,
    }


def complete_analysis(room, session_id):
    session = room["analysis"].get(session_id)

    if not session or session.get("finished"):
        return

    session["finished"] = True

    game = room["game"]

    attacker = get_player(game, session["attacker"])
    victim = get_player(game, session["victim"])

    if attacker:
        attacker.challenge_type = "ready"
        attacker.challenge_target = session["victim_ip"]
        attacker.challenge_firewall = None
        attacker.analyze_cooldown_until = time.time() + ANALYZE_COOLDOWN

        add_activity(
            room,
            attacker,
            "ANALYZE COMPLETE",
            "TARGET ANALYSIS COMPLETE",
        )

    if victim:
        victim.challenge_type = None
        victim.challenge_target = None
        victim.challenge_firewall = None

    add_event(
        room,
        "analysis_complete",
        victim=session["victim"],
    )

    room["analysis"].pop(session_id, None)


def interrupt_analysis(room, session_id):
    session = room["analysis"].get(session_id)

    if not session or session.get("finished"):
        return False

    session["finished"] = True

    game = room["game"]

    attacker = get_player(game, session["attacker"])
    victim = get_player(game, session["victim"])

    if attacker:
        attacker.challenge_type = None
        attacker.challenge_target = None
        attacker.challenge_firewall = None
        attacker.analyze_cooldown_until = time.time() + ANALYZE_COOLDOWN

        add_activity(
            room,
            attacker,
            "ANALYSIS STOPPED",
            "TARGET LOCKED SYSTEM",
        )

    if victim:
        victim.challenge_type = None
        victim.challenge_target = None
        victim.challenge_firewall = None

        add_activity(
            room,
            victim,
            "LOCK",
            "ATTACK BLOCKED",
        )

    add_event(
        room,
        "analysis_interrupted",
        victim=session["victim"],
    )

    room["analysis"].pop(session_id, None)

    return True


def cancel_analysis_for_player(room, player_id):
    for session_id, session in list(room["analysis"].items()):
        if session.get("finished"):
            room["analysis"].pop(session_id, None)
            continue

        if player_id not in (
            session["attacker"],
            session["victim"],
        ):
            continue

        for pid in (
            session["attacker"],
            session["victim"],
        ):
            player = get_player(room["game"], pid)

            if player:
                player.challenge_type = None
                player.challenge_target = None
                player.challenge_firewall = None

        room["analysis"].pop(session_id, None)


def cleanup_analysis(room):
    for session_id, session in list(room["analysis"].items()):
        if session.get("finished"):
            room["analysis"].pop(session_id, None)
            continue

        timer = session.get("timer")
        lock_timer = session.get("lock_completion_timer")

        if timer and timer.is_finished():
            lock_wins = (
                session.get("lock_started", False)
                and lock_timer
                and lock_timer.is_finished()
                and lock_timer.expires_at <= timer.expires_at
            )

            if lock_wins:
                interrupt_analysis(room, session_id)
            else:
                complete_analysis(room, session_id)

            continue

        if (
            session.get("lock_started", False)
            and lock_timer
            and lock_timer.is_finished()
        ):
            interrupt_analysis(room, session_id)


def start_player_analysis(room, attacker, victim):
    now = time.time()

    cooldown_until = getattr(
        attacker,
        "analyze_cooldown_until",
        0,
    )

    if now < cooldown_until:
        return False, (
            f"ERROR: ANALYZE COOLDOWN ACTIVE. "
            f"WAIT {cooldown_until - now:.1f} SECONDS."
        )

    _, active, _ = get_active_analysis_for_player(
        room,
        attacker.player_id,
    )

    if active:
        return False, "ERROR: ANALYSIS ALREADY RUNNING."

    attacker.challenge_type = "analysis"
    attacker.challenge_target = victim.ip

    victim.challenge_type = "being_analyzed"
    victim.challenge_target = attacker.ip

    speed = max(
        1,
        float(getattr(attacker, "speed_multiplier", 1)),
    )

    duration = max(
        0.1,
        random.uniform(
            ANALYSIS_MIN_TIME,
            ANALYSIS_MAX_TIME,
        ) / speed,
    )

    session_id = str(uuid.uuid4())

    room["analysis"][session_id] = {
        "id": session_id,
        "attacker": attacker.player_id,
        "attacker_name": attacker.name,
        "attacker_ip": attacker.ip,
        "victim": victim.player_id,
        "victim_name": victim.name,
        "victim_ip": victim.ip,
        "timer": GameTimer(duration=duration),
        "duration": duration,
        "lock_timer": GameTimer(duration=LOCK_DEFENSE_TIME),
        "lock_started": False,
        "lock_duration": None,
        "lock_completion_timer": None,
        "finished": False,
        "defense_progress": 0,
    }

    add_activity(
        room,
        attacker,
        "ANALYZE",
        "PLAYER TARGET",
    )

    add_activity(
        room,
        victim,
        "UNDER ATTACK",
        "UNKNOWN SOURCE",
    )

    add_event(
        room,
        "analysis_started",
        victim=victim.player_id,
        duration=duration,
    )

    return True, "PLAYER ANALYSIS STARTED. TARGET ANALYSIS RUNNING..."


# =========================================================
# JUMPSCARE
# =========================================================

def maybe_trigger_jumpscare(room):
    if not room.get("started") or room.get("game_over"):
        return False

    if room.get("jumpscare_triggered"):
        return False

    started_at = room.get("game_started_at")

    if not started_at or time.time() - started_at < JUMPSCARE_MIN_DELAY:
        return False

    if time.time() - room.get("last_jumpscare_at", 0) < JUMPSCARE_COOLDOWN:
        return False

    if random.random() > JUMPSCARE_CHANCE:
        return False

    room["jumpscare_triggered"] = True
    room["last_jumpscare_at"] = time.time()

    add_event(room, "jumpscare")

    return True


# =========================================================
# PAGES / LOG
# =========================================================

@app.route("/")
def home():
    return PAGE


@app.route("/loguser", methods=["GET"])
def loguser():
    room_code = request.args.get("room", "").strip()

    if room_code not in rooms:
        return "Room not found.", 404

    room = rooms[room_code]

    cleanup_analysis(room)
    cleanup_game_timer(room)
    update_all_bitcoin_farms(room)

    return build_log_page(room)


# =========================================================
# ROOM CREATION / JOIN
# =========================================================

def make_room(name, account_id=None):
    room_code = generate_room_code()
    player_id = str(uuid.uuid4())

    game = CyberGame()
    game.add_player(player_id, name)

    player = game.players[player_id]

    setup_bitcoin_farm(player)

    if account_id:
        player.account_id = account_id
        load_player_progress(player, account_id)

    rooms[room_code] = {
        "code": room_code,
        "game": game,
        "host": player_id,
        "host_name": name,
        "started": False,
        "host_will_play": True,
        "game_duration_minutes": 15,
        "game_started_at": None,
        "game_ends_at": None,
        "game_over": False,
        "connections": {},
        "events": [],
        "activity": [],
        "analysis": {},
        "jumpscare_triggered": False,
        "last_jumpscare_at": 0,
    }

    return room_code, player_id


@app.route("/api/create", methods=["POST"])
def create_room():
    data = request.get_json(silent=True) or {}

    name = str(data.get("name", "")).strip()

    if not name:
        return jsonify({
            "success": False,
            "error": "Player name is required.",
        }), 400

    account = account_for_request()

    if request_token() and not account:
        return session_expired_response()

    account_id = account["id"] if account else None

    room_code, player_id = make_room(name, account_id)

    return jsonify({
        "success": True,
        "room": room_code,
        "player": player_id,
    })


@app.route("/api/join", methods=["POST"])
def join_room():
    data = request.get_json(silent=True) or {}

    room_code = str(data.get("room", "")).strip()
    name = str(data.get("name", "")).strip()

    if not room_code or not name:
        return jsonify({
            "success": False,
            "error": "Room code and player name are required.",
        }), 400

    if room_code not in rooms:
        return jsonify({
            "success": False,
            "error": "Room not found.",
        }), 404

    room = rooms[room_code]

    if room["started"]:
        return jsonify({
            "success": False,
            "error": "Game has already started.",
        }), 400

    account = account_for_request()

    if request_token() and not account:
        return session_expired_response()

    player_id = str(uuid.uuid4())

    room["game"].add_player(player_id, name)

    player = room["game"].players[player_id]

    setup_bitcoin_farm(player)

    if account:
        player.account_id = account["id"]
        load_player_progress(player, account["id"])

    add_activity(
        room,
        player,
        "JOINED",
        "JOINED THE LOBBY",
    )

    return jsonify({
        "success": True,
        "room": room_code,
        "player": player_id,
    })


# =========================================================
# HOST CONTROLS
# =========================================================

@app.route("/api/host-play", methods=["POST"])
def host_play():
    data = request.get_json(silent=True) or {}

    room_code = str(data.get("room", "")).strip()
    player_id = str(data.get("player", "")).strip()
    value = bool(data.get("value", True))

    if room_code not in rooms:
        return jsonify({
            "success": False,
            "error": "Room not found.",
        }), 404

    room = rooms[room_code]

    if player_id != room["host"]:
        return jsonify({
            "success": False,
            "error": "Only the host can change this.",
        }), 403

    if room["started"]:
        return jsonify({
            "success": False,
            "error": "Game has already started.",
        }), 400

    room["host_will_play"] = value

    game = room["game"]

    if not value:
        cancel_analysis_for_player(room, player_id)
        room["connections"].pop(player_id, None)
        game.players.pop(player_id, None)

    elif player_id not in game.players:
        game.add_player(player_id, room["host_name"])
        setup_bitcoin_farm(game.players[player_id])

    return jsonify({
        "success": True,
        "host_will_play": value,
    })


@app.route("/api/game-time", methods=["POST"])
def game_time():
    data = request.get_json(silent=True) or {}

    room_code = str(data.get("room", "")).strip()
    player_id = str(data.get("player", "")).strip()

    try:
        minutes = int(data.get("minutes", 15))
    except (ValueError, TypeError):
        return jsonify({
            "success": False,
            "error": "Invalid game time.",
        }), 400

    if room_code not in rooms:
        return jsonify({
            "success": False,
            "error": "Room not found.",
        }), 404

    room = rooms[room_code]

    if player_id != room["host"]:
        return jsonify({
            "success": False,
            "error": "Only the host can change the game time.",
        }), 403

    if room["started"]:
        return jsonify({
            "success": False,
            "error": "Game has already started.",
        }), 400

    if minutes not in ALLOWED_GAME_TIMES:
        return jsonify({
            "success": False,
            "error": "Invalid game time.",
        }), 400

    room["game_duration_minutes"] = minutes

    return jsonify({
        "success": True,
        "game_duration_minutes": minutes,
    })


@app.route("/api/start", methods=["POST"])
def start_game():
    data = request.get_json(silent=True) or {}

    room_code = str(data.get("room", "")).strip()
    player_id = str(data.get("player", "")).strip()

    if room_code not in rooms:
        return jsonify({
            "success": False,
            "error": "Room not found.",
        }), 404

    room = rooms[room_code]

    if player_id != room["host"]:
        return jsonify({
            "success": False,
            "error": "Only the host can start the game.",
        }), 403

    if room["started"]:
        return jsonify({
            "success": False,
            "error": "Game has already started.",
        }), 400

    if not room.get("host_will_play", True):
        room["game"].players.pop(room["host"], None)
        room["connections"].pop(room["host"], None)

    minutes = room.get("game_duration_minutes", 15)

    now = time.time()

    room["game_started_at"] = now
    room["game_ends_at"] = now + minutes * 60
    room["game_over"] = False
    room["started"] = True
    room["jumpscare_triggered"] = False
    room["last_jumpscare_at"] = 0

    for player in room["game"].players.values():
        setup_bitcoin_farm(player)

        player.farm_last_update = now
        player.current_ip = "10.0.0.99"
        player.challenge_type = None
        player.challenge_target = None
        player.challenge_firewall = None
        player.analyze_cooldown_until = 0

        room["connections"][player.player_id] = ["10.0.0.99"]

        add_activity(
            room,
            player,
            "READY",
            "GAME STARTED",
        )

    add_event(
        room,
        "system",
        message="GAME STARTED.",
    )

    return jsonify({
        "success": True,
        "game_duration_minutes": minutes,
    })


# =========================================================
# MOTHERBOARD HARDWARE PURCHASE / INSTALLATION
# =========================================================

@app.route("/api/hardware/purchase", methods=["POST"])
def purchase_hardware_component():
    data = request.get_json(silent=True) or {}

    room_code = str(data.get("room", "")).strip()
    player_id = str(data.get("player", "")).strip()
    part_type = str(data.get("part", "")).strip().lower()

    if part_type not in HARDWARE_PARTS:
        return jsonify({
            "success": False,
            "error": "Choose CPU, RAM or STORAGE.",
        }), 400

    if room_code not in rooms:
        return jsonify({
            "success": False,
            "error": "Room not found.",
        }), 404

    room = rooms[room_code]

    if not room.get("started"):
        return jsonify({
            "success": False,
            "error": "GAME HAS NOT STARTED.",
        }), 400

    cleanup_game_timer(room)

    if room.get("game_over"):
        return jsonify({
            "success": False,
            "error": "GAME OVER.",
        }), 400

    player = get_player(room["game"], player_id)

    if not player:
        return jsonify({
            "success": False,
            "error": "PLAYER SESSION NOT FOUND.",
        }), 404

    normalize_hardware(player)
    update_bitcoin_farm(player)

    config = HARDWARE_PARTS[part_type]

    installed = player.hardware_slots.get(part_type) or {}

    highest_tier = max(
        1,
        int(installed.get(
            "tier",
            getattr(player, config["level_attr"], 1),
        )),
    )

    for item in player.hardware_inventory:
        if item.get("type") == part_type:
            highest_tier = max(
                highest_tier,
                int(item.get("tier", 1)),
            )

    price = config["base_price"] * highest_tier

    if player.economy.coins < price:
        return jsonify({
            "success": False,
            "error": (
                f"NOT ENOUGH COINS. "
                f"{config['name']} COMPONENT COSTS {price} COINS."
            ),
            "coins": player.economy.coins,
            "hardware": hardware_payload(player),
        }), 400

    component = make_hardware_component(
        part_type,
        highest_tier + 1,
    )

    player.economy.coins -= price
    player.hardware_inventory.append(component)

    save_player_progress(player)

    add_activity(
        room,
        player,
        "HARDWARE PURCHASED",
        f"{component['name']} added to inventory | -{price} COINS",
    )

    return jsonify({
        "success": True,
        "message": (
            f"{component['name']} BOUGHT. "
            f"RIGHT-CLICK THE MATCHING MOTHERBOARD SLOT TO INSTALL IT."
        ),
        "coins": player.economy.coins,
        "hardware": hardware_payload(player),
        "bitcoin_farm": bitcoin_farm_data(player),
    })


@app.route("/api/hardware/install", methods=["POST"])
def install_hardware_component():
    data = request.get_json(silent=True) or {}

    room_code = str(data.get("room", "")).strip()
    player_id = str(data.get("player", "")).strip()
    slot_key = str(data.get("slot", "")).strip().lower()

    if slot_key not in HARDWARE_SLOT_TYPES:
        return jsonify({
            "success": False,
            "error": "Invalid motherboard slot.",
        }), 400

    if room_code not in rooms:
        return jsonify({
            "success": False,
            "error": "Room not found.",
        }), 404

    room = rooms[room_code]

    if not room.get("started"):
        return jsonify({
            "success": False,
            "error": "GAME HAS NOT STARTED.",
        }), 400

    cleanup_game_timer(room)

    if room.get("game_over"):
        return jsonify({
            "success": False,
            "error": "GAME OVER.",
        }), 400

    player = get_player(room["game"], player_id)

    if not player:
        return jsonify({
            "success": False,
            "error": "PLAYER SESSION NOT FOUND.",
        }), 404

    normalize_hardware(player)
    update_bitcoin_farm(player)

    expected_type = HARDWARE_SLOT_TYPES[slot_key]

    candidates = [
        item
        for item in player.hardware_inventory
        if item.get("type") == expected_type
    ]

    if not candidates:
        occupied = player.hardware_slots.get(slot_key)

        if isinstance(occupied, dict):
            message = (
                f"{occupied.get('name', expected_type.upper())} "
                f"IS ALREADY INSTALLED. BUY A REPLACEMENT OF THAT TYPE "
                f"TO SWAP IT."
            )
        else:
            message = (
                f"NO {expected_type.upper()} IN YOUR HARDWARE INVENTORY. "
                f"BUY ONE IN THE COMPONENTS TAB FIRST."
            )

        return jsonify({
            "success": False,
            "error": message,
            "coins": player.economy.coins,
            "hardware": hardware_payload(player),
            "bitcoin_farm": bitcoin_farm_data(player),
        }), 400

    component = max(
        candidates,
        key=lambda item: int(item.get("tier", 1)),
    )

    player.hardware_inventory.remove(component)

    current = player.hardware_slots.get(slot_key)

    if isinstance(current, dict):
        player.hardware_inventory.append(current)

    player.hardware_slots[slot_key] = component

    sync_hardware_stats(player)

    player.farm_last_update = time.time()
    player.farm_running = bool(
        getattr(player, "gpu_count", 0) > 0
    )

    save_player_progress(player)

    add_activity(
        room,
        player,
        "HARDWARE INSTALLED",
        f"{component['name']} installed in {slot_key.upper()}",
    )

    add_event(
        room,
        "hardware_installed",
        player=player.player_id,
        slot=slot_key,
        component=component["name"],
    )

    return jsonify({
        "success": True,
        "message": f"{component['name']} INSTALLED IN {slot_key.upper()}.",
        "coins": player.economy.coins,
        "hardware": hardware_payload(player),
        "bitcoin_farm": bitcoin_farm_data(player),
    })


# =========================================================
# BUY GPU
# =========================================================

@app.route("/api/buy-gpu", methods=["POST"])
def buy_gpu():
    data = request.get_json(silent=True) or {}

    room_code = str(data.get("room", "")).strip()
    player_id = str(data.get("player", "")).strip()

    if room_code not in rooms:
        return jsonify({
            "success": False,
            "error": "Room not found.",
        }), 404

    room = rooms[room_code]

    if not room.get("started"):
        return jsonify({
            "success": False,
            "error": "GAME HAS NOT STARTED.",
        }), 400

    cleanup_game_timer(room)

    if room.get("game_over"):
        return jsonify({
            "success": False,
            "error": "GAME OVER.",
        }), 400

    player = get_player(room["game"], player_id)

    if not player:
        return jsonify({
            "success": False,
            "error": "PLAYER SESSION NOT FOUND.",
        }), 404

    normalize_hardware(player)
    update_bitcoin_farm(player)

    price = get_gpu_price(player)

    if player.economy.coins < price:
        return jsonify({
            "success": False,
            "error": f"NOT ENOUGH COINS. GPU COSTS {price} COINS.",
            "bitcoin_farm": bitcoin_farm_data(player),
            "coins": player.economy.coins,
            "hardware": hardware_payload(player),
        }), 400

    player.economy.coins -= price

    player.hardware_inventory.append(
        make_hardware_component("gpu", 1)
    )

    player.farm_last_update = time.time()

    save_player_progress(player)

    add_activity(
        room,
        player,
        "GPU PURCHASED",
        f"GPU added to hardware inventory | -{price} COINS",
    )

    add_event(
        room,
        "gpu_purchased",
        player=player.player_id,
        player_name=player.name,
        inventory=True,
    )

    return jsonify({
        "success": True,
        "message": (
            "GPU BOUGHT. RIGHT-CLICK AN EMPTY GPU SLOT "
            "IN MOTHERBOARD TO INSTALL IT."
        ),
        "coins": player.economy.coins,
        "bitcoin_farm": bitcoin_farm_data(player),
        "hardware": hardware_payload(player),
    })


# =========================================================
# STATE
# =========================================================

@app.route("/api/state/<room_code>", methods=["GET"])
def get_state(room_code):
    if room_code not in rooms:
        return jsonify({
            "success": False,
            "error": "Room not found.",
        }), 404

    room = rooms[room_code]

    cleanup_analysis(room)
    cleanup_game_timer(room)
    maybe_trigger_jumpscare(room)

    # Update farms and perform throttled passive saves once.
    update_all_bitcoin_farms(room)

    game = room["game"]

    current_player_id = request.args.get("player", "")
    current_player = get_player(game, current_player_id)

    remaining = 0

    if room.get("game_ends_at") and not room.get("game_over"):
        remaining = max(
            0,
            int(room["game_ends_at"] - time.time()),
        )

    players = [
        player_data(player)
        for player in game.players.values()
    ]

    # Reuse the player payload instead of serializing it twice.
    current_player_data = next(
        (
            data
            for data in players
            if data["player_id"] == current_player_id
        ),
        None,
    )

    valid_ips = set(game.computers.keys())
    valid_ips.update(
        player.ip
        for player in game.players.values()
    )

    for source_id, targets in list(room["connections"].items()):
        if isinstance(targets, str):
            targets = [targets]

        targets = [
            ip
            for ip in targets
            if ip in valid_ips
        ]

        if targets:
            room["connections"][source_id] = targets
        else:
            room["connections"].pop(source_id, None)

    connections = []

    for computer_ip in game.computers:
        if computer_ip != "10.0.0.99":
            connections.append([
                computer_ip,
                "10.0.0.99",
            ])

    if room["started"]:
        for player in game.players.values():
            connections.append([
                player.ip,
                "10.0.0.99",
            ])

    for source_id, targets in room["connections"].items():
        source = get_player(game, source_id)

        if not source:
            continue

        if isinstance(targets, str):
            targets = [targets]

        for target_ip in targets:
            if target_ip == "10.0.0.99":
                continue

            target = game.find_target(target_ip)

            if target and hasattr(target, "player_id"):
                continue

            connections.append([
                source.ip,
                target_ip,
            ])

    is_host = current_player_id == room["host"]

    activity = (
        room.get("activity", [])[-100:]
        if is_host
        else []
    )

    visible_events = []

    for event in room.get("events", [])[-50:]:
        event_copy = dict(event)

        if event_copy.get("type") == "hack_detected":
            if event_copy.get("victim") == current_player_id:
                visible_events.append({
                    "id": event_copy["id"],
                    "type": "hack_detected",
                    "time": event_copy["time"],
                    "victim": current_player_id,
                    "message": "HACK_DETECTED",
                })

            elif event_copy.get("attacker_id") == current_player_id:
                visible_events.append({
                    "id": event_copy["id"],
                    "type": "hack_success",
                    "time": event_copy["time"],
                    "message": "HACK SUCCESSFUL",
                })

            else:
                visible_events.append({
                    "id": event_copy["id"],
                    "type": "system",
                    "time": event_copy["time"],
                    "message": "NETWORK ACTIVITY DETECTED",
                })

        elif event_copy.get("type") == "analysis_started":
            if event_copy.get("victim") == current_player_id:
                visible_events.append({
                    "id": event_copy["id"],
                    "type": "analysis_started",
                    "time": event_copy["time"],
                    "victim": current_player_id,
                })
            else:
                visible_events.append(event_copy)

        else:
            visible_events.append(event_copy)

    return jsonify({
        "success": True,
        "room": room_code,
        "started": room["started"],
        "host": room["host"],
        "host_will_play": room.get("host_will_play", True),
        "game_duration_minutes": room.get("game_duration_minutes", 15),
        "game_time_remaining": remaining,
        "game_over": room.get("game_over", False),
        "players": players,
        "player": current_player_data,
        "connections": connections,
        "analysis": analysis_state(room, current_player_id),
        "leaderboard": get_leaderboard(room),
        "teams": public_teams(game),
        "events": visible_events[-20:],
        "is_host": is_host,
        "activity": activity,
        "jumpscare": room.get("jumpscare_triggered", False),
    })


# =========================================================
# COMMANDS
# =========================================================

@app.route("/api/command", methods=["POST"])
def command():
    data = request.get_json(silent=True) or {}

    room_code = str(data.get("room", "")).strip()
    player_id = str(data.get("player", "")).strip()
    text = str(data.get("command", "")).strip()

    if room_code not in rooms:
        return jsonify({
            "output": "ERROR: ROOM NOT FOUND.",
        }), 404

    room = rooms[room_code]

    if not room["started"]:
        return jsonify({
            "output": "GAME HAS NOT STARTED.",
        }), 400

    cleanup_game_timer(room)

    if room.get("game_over"):
        return jsonify({
            "output": (
                "GAME OVER.\n"
                "THE FINAL LEADERBOARD IS NOW AVAILABLE."
            ),
        })

    game = room["game"]

    player = get_player(game, player_id)

    if not player:
        return jsonify({
            "output": "PLAYER SESSION NOT FOUND.",
        }), 404

    if not text:
        return jsonify({"output": ""})

    update_bitcoin_farm(player)
    cleanup_analysis(room)

    parts = text.split()
    command_name = parts[0].lower().rstrip(":")

    if command_name == "lock":
        session_id, session, role = get_active_analysis_for_player(
            room,
            player_id,
        )

        if not session or role != "victim":
            add_activity(
                room,
                player,
                "LOCK FAILED",
                "NO ACTIVE ATTACK",
            )

            return jsonify({
                "output": "ERROR: NO ACTIVE ANALYSIS TO LOCK.",
            })

        if session["timer"].is_finished():
            complete_analysis(room, session_id)

            return jsonify({
                "output": "TOO LATE. ANALYSIS COMPLETE.",
            })

        window = session.get("lock_timer")

        if window and window.is_finished():
            complete_analysis(room, session_id)

            return jsonify({
                "output": "TOO LATE. LOCK WINDOW EXPIRED.",
            })

        if session.get("lock_started"):
            timer = session.get("lock_completion_timer")

            if timer and not timer.is_finished():
                return jsonify({
                    "output": (
                        f"LOCK ALREADY IN PROGRESS. "
                        f"WAIT {timer.remaining():.1f} SECONDS."
                    ),
                })

        duration = random.uniform(
            LOCK_MIN_TIME,
            LOCK_MAX_TIME,
        )

        session["lock_started"] = True
        session["lock_duration"] = duration
        session["lock_completion_timer"] = GameTimer(
            duration=duration
        )
        session["defense_progress"] = 1

        add_activity(
            room,
            player,
            "LOCK STARTED",
            f"{duration:.1f} SECOND LOCK",
        )

        add_event(
            room,
            "lock_started",
            victim=session["victim"],
            duration=duration,
        )

        return jsonify({
            "output": (
                f"SYSTEM LOCK INITIATED.\n"
                f"LOCKING... {duration:.1f} SECONDS.\n"
                f"DO NOT INTERRUPT."
            ),
        })

    if command_name == "connect" and len(parts) >= 2:
        target_ip = parts[1]
        target = game.find_target(target_ip)

        if not target:
            add_activity(
                room,
                player,
                "CONNECT FAILED",
                target_ip,
            )

            return jsonify({
                "output": "Host not found: " + target_ip,
            })

        if target_ip == player.ip:
            return jsonify({
                "output": "You cannot connect to yourself.",
            })

        cancel_analysis_for_player(room, player_id)

        player.current_ip = target_ip

        if not hasattr(target, "player_id"):
            room["connections"].setdefault(
                player_id,
                [],
            )

            if target_ip not in room["connections"][player_id]:
                room["connections"][player_id].append(target_ip)

        output = game.command(player, text)

        add_activity(
            room,
            player,
            "CONNECT",
            target_ip,
        )

        return jsonify({
            "output": str(output or ""),
        })

    if command_name in ("disconnect", "dc"):
        cancel_analysis_for_player(room, player_id)

        room["connections"].pop(player_id, None)

        output = game.command(player, "disconnect")

        add_activity(
            room,
            player,
            "DISCONNECT",
            "",
        )

        return jsonify({
            "output": str(output or ""),
        })

    if command_name == "analyze":
        _, active, _ = get_active_analysis_for_player(
            room,
            player_id,
        )

        if active:
            return jsonify({
                "output": "ERROR: ANALYSIS ALREADY RUNNING.",
            })

        cooldown = (
            getattr(player, "analyze_cooldown_until", 0)
            - time.time()
        )

        if cooldown > 0:
            return jsonify({
                "output": (
                    f"ERROR: ANALYZE COOLDOWN ACTIVE.\n"
                    f"WAIT {cooldown:.1f} SECONDS."
                ),
            })

        target = game.find_target(player.current_ip)

        if target and hasattr(target, "player_id"):
            if target.player_id == player.player_id:
                return jsonify({
                    "output": "You cannot analyze yourself.",
                })

            if game.same_team(player, target):
                return jsonify({
                    "output": (
                        "ERROR: TEAMMATE NODE. "
                        "YOU CANNOT ATTACK YOUR OWN TEAM."
                    ),
                })

            _, output = start_player_analysis(
                room,
                player,
                target,
            )

            return jsonify({"output": output})

        output = game.command(player, text)

        return jsonify({
            "output": str(output or ""),
        })

    if command_name == "traceback":
        output = game.command(player, text)

        save_player_progress(player)

        add_activity(
            room,
            player,
            "TRACEBACK",
            "TRACEBACK ATTEMPTED",
        )

        return jsonify({
            "output": str(output or ""),
        })

    output = game.command(player, text)
    output = str(output or "")

    add_activity(
        room,
        player,
        command_name,
        output[:160],
    )

    victim_id = getattr(
        game,
        "last_hacked_player",
        None,
    )

    if command_name in ("hack", "teamhack") and victim_id:
        victim = get_player(game, victim_id)

        stolen = int(
            getattr(game, "last_hack_stolen", 0)
        )

        add_event(
            room,
            "hack_detected",
            victim=victim_id,
            victim_name=victim.name if victim else "UNKNOWN",
            attacker_id=player.player_id,
            stolen=stolen,
            remaining=victim.economy.coins if victim else 0,
            message="HACK_DETECTED",
        )

        add_activity(
            room,
            player,
            "HACK SUCCESS",
            f"COINS STOLEN: {stolen}",
        )

        if victim:
            add_activity(
                room,
                victim,
                "HACKED",
                "UNKNOWN SOURCE",
            )

    if command_name in (
        "buy",
        "upgrade",
        "store",
        "inventory",
        "hardware",
        "ddos",
        "mitm",
    ):
        add_activity(
            room,
            player,
            command_name,
            output[:160],
        )

    if (
        command_name in ("ddos", "mitm")
        and "SUCCESSFUL" in output
    ):
        add_event(
            room,
            "simulated_attack",
            attack=command_name,
            attacker=player.player_id,
            message=output.splitlines()[0],
        )

        target = (
            game.find_target(parts[1])
            if len(parts) > 1
            else None
        )

        if target and hasattr(target, "player_id"):
            add_activity(
                room,
                target,
                "UNDER ATTACK",
                f"SIMULATED {command_name.upper()} EVENT",
            )

            save_player_progress(target)

    save_player_progress(player)

    if victim_id:
        victim = get_player(game, victim_id)

        if victim:
            save_player_progress(victim)

    for helper_id in getattr(game, "last_hack_helpers", []):
        helper = get_player(game, helper_id)

        if helper:
            save_player_progress(helper)

    return jsonify({
        "output": output,
    })


# =========================================================
# SERVER START
# =========================================================

if __name__ == "__main__":
    local_ip = get_local_ip()
    port = int(os.environ.get("PORT", 5000))

    print()
    print("========================================")
    print("          CYBER//NET SERVER")
    print("========================================")
    print()
    print("PC:")
    print(f"http://127.0.0.1:{port}")
    print()
    print("MOBILE / LAN:")
    print(f"http://{local_ip}:{port}")
    print()
    print("========================================")
    print()

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
    )
