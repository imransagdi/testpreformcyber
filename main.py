import random
import time

from firewall import Firewall
from update import PlayerEconomy
from storeitems import get_store_items, format_store


RANKS = [
    (0, "SCRIPT KIDDIE"),
    (100, "BLACK HAT"),
    (300, "ELITE HACKER"),
    (600, "PHANTOM"),
    (1000, "GHOST"),
]

BLACK_MARKET = {
    "disguise": 300,
    "ip_reroll": 200,
    "firewall_patch": 250,
    "counter_hack": 350,
    "traceback_tool": 300,
}


# Teams
TEAM_TYPES = {"duo": 2, "trio": 3, "quadro": 4}
TEAM_SUB_PRICE = 5000
TEAM_SUB_BASE_FIREWALL = 5
TEAM_SUB_BREACH_SECONDS = 30
DEFAULT_TEAM_NAMES = ["ALPHA", "BRAVO", "CHARLIE", "DELTA", "ECHO", "FOXTROT", "GOLF", "HOTEL"]
TEAM_USAGE = (
    "TEAM COMMANDS\n"
    "team                     - show your team\n"
    "team list                - list all teams\n"
    "team create [duo|trio|quadro] [name]\n"
    "team join [name]\n"
    "team leave\n"
    "team kick [player name]  - leader only\n"
    f"team sub                 - leader buys the SUB MAINFRAME ({TEAM_SUB_PRICE} coins)\n"
    "teamhack [amount]        - hack together with teammates connected to the same target"
)


class Computer:
    def __init__(self, name, ip, firewall_level, ports, files):
        self.name = name
        self.ip = ip
        self.firewall = Firewall(firewall_level)
        self.ports = list(ports)
        self.files = dict(files)
        self.hacked = False
        self.attacker = None


class SubMainframe(Computer):
    """A team's own simulated mainframe node. Its firewall comes from the team."""

    def __init__(self, team, ip):
        super().__init__(
            f"SUB-{team.name}.HOST",
            ip,
            TEAM_SUB_BASE_FIREWALL,
            [22, 80, 443],
            {"readme.txt": f"SUB MAINFRAME OF TEAM {team.name}. SIMULATED ONLY."},
        )
        self.is_sub = True
        self.team = team


class Team:
    def __init__(self, team_id, name, team_type, leader):
        self.team_id = team_id
        self.name = name
        self.team_type = team_type
        self.max_members = TEAM_TYPES[team_type]
        self.leader = leader
        self.members = [leader]
        self.sub = None
        self.breached_until = 0.0

    def firewall_level(self):
        return TEAM_SUB_BASE_FIREWALL + len(self.members)

    def shield_active(self):
        return self.sub is not None and time.time() >= self.breached_until

    def breach_remaining(self):
        return max(0.0, self.breached_until - time.time())


class Player:
    def __init__(self, player_id, name, ip):
        self.player_id = player_id
        self.name = name
        self.ip = ip
        self.economy = PlayerEconomy()

        self.current_ip = "10.0.0.99"
        self.challenge = None
        self.challenge_type = None
        self.challenge_target = None
        self.challenge_firewall = None

        self.detection = 0
        self.ports = [22, 80, 443]
        self.hacked = False
        self.attacker = None
        self.hacks_done = 0

        self.speed_multiplier = 1
        self.speed_upgrade_level = 0
        self.firewall_upgrade_level = 0
        self.exploit_upgrade_level = 0

        self.reputation = 0
        self.account_id = None
        self.team = None
        self.disguised = False
        self.disguise_name = None
        self.attack_history = []
        self.last_attackers = []
        self.traceback_cooldown = 0
        self.ddos_owned = False
        self.mitm_owned = False
        self.ddos_cooldown_until = 0.0
        self.mitm_cooldown_until = 0.0
        self.ddos_disabled_until = 0.0
        self.cpu_level = 1
        self.ram_level = 1
        self.storage_level = 1

        # Hardware components installed on the simulated motherboard.
        self.hardware_slots = {
            "cpu": {"id": "factory-cpu", "type": "cpu", "tier": 1, "name": "Factory CPU T1"},
            "ram": {"id": "factory-ram", "type": "ram", "tier": 1, "name": "Factory RAM T1"},
            "storage": {"id": "factory-storage", "type": "storage", "tier": 1, "name": "Factory Storage T1"},
            "gpu1": None,
            "gpu2": None,
            "gpu3": None,
            "gpu4": None,
        }
        self.hardware_inventory = []

    def get_rank(self):
        rank = "SCRIPT KIDDIE"
        for threshold, name in RANKS:
            if self.reputation >= threshold:
                rank = name
        return rank


class CyberGame:
    def __init__(self):
        self.computers = {}
        self.players = {}
        self.last_hacked_player = None
        self.last_hack_stolen = 0
        self.last_hack_helpers = []
        self.attack_records = []
        self.teams = {}
        self.team_counter = 0
        self.create_network()

    def create_network(self):
        self.computers = {
            "10.0.0.15": Computer(
                "PC-01",
                "10.0.0.15",
                2,
                [22, 80],
                {
                    "readme.txt": "Welcome to PC-01.",
                    "notes.txt": "Nothing important here.",
                    "userdata.dat": "SIMULATED USER DATA ONLY.",
                },
            ),
            "10.0.0.20": Computer(
                "SERVER-02",
                "10.0.0.20",
                4,
                [22, 80, 443],
                {
                    "readme.txt": "SERVER-02 system files.",
                    "users.txt": "User database access restricted.",
                    "userdata.dat": "SIMULATED USER DATA ONLY.",
                },
            ),
            "10.0.0.31": Computer(
                "LAPTOP-07",
                "10.0.0.31",
                3,
                [22, 443],
                {
                    "readme.txt": "LAPTOP-07 private files.",
                    "backup.txt": "Backup data.",
                    "userdata.dat": "SIMULATED USER DATA ONLY.",
                },
            ),
            "10.0.0.99": Computer(
                "MAINFRAME.HOST",
                "10.0.0.99",
                8,
                [22, 80, 443],
                {
                    "readme.txt": "CYBER//NET MAINFRAME.",
                    "system.log": "Mainframe log access restricted.",
                },
            ),
        }

    def add_player(self, player_id, name):
        while True:
            ip = f"10.0.0.{random.randint(100, 250)}"
            if ip not in self.computers and not any(
                p.ip == ip for p in self.players.values()
            ):
                break

        player = Player(player_id, name, ip)
        self.players[player_id] = player
        return player

    def find_player(self, player_id):
        return self.players.get(str(player_id))

    def find_target(self, ip):
        ip = str(ip).strip()
        if ip in self.computers:
            return self.computers[ip]
        for player in self.players.values():
            if player.ip == ip:
                return player
        return None

    def get_current_target(self, player):
        if not player.challenge_target:
            return None
        return self.find_target(player.challenge_target)

    def get_current_computer(self, player):
        target = self.get_current_target(player)
        return target if isinstance(target, Computer) else None

    def get_firewall_level(self, target):
        ddos_active = time.time() < getattr(target, "ddos_disabled_until", 0)
        if isinstance(target, Player):
            level = target.economy.firewall_level
            team = getattr(target, "team", None)
            if team is not None and team.shield_active():
                level = max(level, team.firewall_level())
            return max(0, level - 3) if ddos_active else level
        if isinstance(target, Computer):
            if getattr(target, "is_sub", False):
                level = target.team.firewall_level()
            else:
                level = int(getattr(target.firewall, "level", 1))
            return max(0, level - 3) if ddos_active else level
        return 0

    # -----------------------------------------------------------------
    # TEAM HELPERS
    # -----------------------------------------------------------------

    def same_team(self, first, second):
        return (
            isinstance(first, Player)
            and isinstance(second, Player)
            and first.team is not None
            and first.team is second.team
        )

    def team_helpers(self, player, target):
        """Teammates currently connected to the same target as this player."""
        team = getattr(player, "team", None)
        if team is None or target is None:
            return []
        return [
            member for member in team.members
            if member is not player
            and member.player_id in self.players
            and getattr(member, "current_ip", None) == target.ip
        ]

    def exploit_power(self, player, target):
        return player.economy.exploit_level + len(self.team_helpers(player, target))

    def give_coins(self, player, amount):
        amount = max(0, int(amount))
        player.economy.coins += amount
        return amount

    def get_leaderboard(self):
        players = sorted(
            self.players.values(),
            key=lambda p: (p.economy.coins, p.hacks_done),
            reverse=True,
        )
        return [
            {
                "id": p.player_id,
                "name": p.name,
                "coins": p.economy.coins,
                "hacks": p.hacks_done,
                "rank": p.get_rank(),
                "reputation": p.reputation,
            }
            for p in players
        ]

    def upgrade(self, player, upgrade):
        upgrade = upgrade.lower().strip()

        # Hardware upgrades are bought as spare components now. They only
        # affect the machine after the component is installed on the board.
        if upgrade in ("cpu", "ram", "storage"):
            inventory = getattr(player, "hardware_inventory", None)
            if not isinstance(inventory, list):
                inventory = []
                player.hardware_inventory = inventory
            slots = getattr(player, "hardware_slots", {})
            installed = slots.get(upgrade) if isinstance(slots, dict) else None
            tier = max(1, int(installed.get("tier", 1))) if isinstance(installed, dict) else max(
                1, int(getattr(player, {"cpu": "cpu_level", "ram": "ram_level", "storage": "storage_level"}[upgrade], 1))
            )
            for item in inventory:
                if isinstance(item, dict) and item.get("type") == upgrade:
                    tier = max(tier, int(item.get("tier", 1)))
            base_price = {"cpu": 250, "ram": 400, "storage": 300}[upgrade]
            price = base_price * tier
            if player.economy.coins < price:
                return f"Not enough coins. Need {price}."
            player.economy.coins -= price
            next_tier = tier + 1
            component_id = f"cli-{upgrade}-{random.randint(100000, 999999)}"
            inventory.append({
                "id": component_id,
                "type": upgrade,
                "tier": next_tier,
                "name": f"{upgrade.upper()} T{next_tier}",
            })
            return (
                f"{upgrade.upper()} T{next_tier} PURCHASED INTO HARDWARE INVENTORY. "
                "Open MOTHERBOARD and right-click the matching slot to install it. "
                f"Coins left: {player.economy.coins}"
            )

        prices = {
            "speed": 100 * (player.speed_upgrade_level + 1),
            "firewall": 150 * (player.firewall_upgrade_level + 1),
            "exploit": 150 * (player.exploit_upgrade_level + 1),
        }
        if upgrade not in prices:
            return "Unknown upgrade. Use speed, firewall, exploit, cpu, ram, or storage."

        price = prices[upgrade]
        if player.economy.coins < price:
            return f"Not enough coins. Need {price}."

        player.economy.coins -= price

        if upgrade == "speed":
            player.speed_upgrade_level += 1
            player.speed_multiplier += 0.25
        elif upgrade == "firewall":
            player.firewall_upgrade_level += 1
            player.economy.firewall_level += 1
        elif upgrade == "exploit":
            player.exploit_upgrade_level += 1
            player.economy.exploit_level += 1
        return f"{upgrade.upper()} UPGRADED. Coins left: {player.economy.coins}"

    def scan(self, player):
        lines = ["NETWORK SCAN", "-------------"]

        # Do not show computers that have already been compromised.
        for computer in self.computers.values():
            if getattr(computer, "hacked", False):
                continue

            lines.append(
                f"{computer.name} | {computer.ip} | "
                f"FIREWALL {self.get_firewall_level(computer)}"
            )

        # Do not show yourself or player nodes that are already compromised.
        for target in self.players.values():
            if target.player_id == player.player_id or getattr(target, "hacked", False):
                continue

            if self.same_team(player, target):
                lines.append(f"TEAMMATE {target.name} | {target.ip}")
            else:
                lines.append(
                    f"PLAYER NODE | {target.ip} | FIREWALL UNKNOWN"
                )

        return "\n".join(lines)

    def connect(self, player, args):
        if not args:
            return "Usage: connect [IP]"

        target = self.find_target(args[0])
        if target is None:
            return "Target not found."

        player.current_ip = target.ip
        player.challenge_target = target.ip
        player.challenge = None
        player.challenge_type = None

        return f"CONNECTED TO {target.ip}"

    def disconnect(self, player):
        player.current_ip = "10.0.0.99"
        player.challenge = None
        player.challenge_type = None
        player.challenge_target = None
        player.challenge_firewall = None
        return "DISCONNECTED. Returned to MAINFRAME.HOST."

    def info(self, player, args):
        if args:
            target = self.find_target(args[0])
        else:
            target = self.get_current_target(player)

        if target is None:
            return (
                f"PLAYER: {player.name}\n"
                f"IP: {player.ip}\n"
                f"RANK: {player.get_rank()}\n"
                f"REPUTATION: {player.reputation}\n"
                f"COINS: {player.economy.coins}"
            )

        if isinstance(target, Player):
            return (
                f"PLAYER NODE\n"
                f"IP: {target.ip}\n"
                f"FIREWALL: {self.get_firewall_level(target)}\n"
                "IDENTITY: ENCRYPTED"
            )

        return (
            f"NAME: {target.name}\n"
            f"IP: {target.ip}\n"
            f"FIREWALL: {self.get_firewall_level(target)}\n"
            f"PORTS: {', '.join(map(str, target.ports))}"
        )

    def ports(self, player, args):
        target = self.find_target(args[0]) if args else self.get_current_target(player)
        if target is None:
            return f"Your open ports: {', '.join(map(str, player.ports))}"
        return f"OPEN PORTS: {', '.join(map(str, target.ports))}"

    def probe(self, player, args):
        target = self.find_target(args[0]) if args else self.get_current_target(player)
        if target is None:
            return "No target selected."
        return (
            f"PROBE COMPLETE: {target.ip}\n"
            f"FIREWALL LEVEL: {self.get_firewall_level(target)}\n"
            f"OPEN PORTS: {', '.join(map(str, target.ports))}"
        )

    def analyze(self, player, args):
        if not args:
            target = self.get_current_target(player)
        else:
            target = self.find_target(args[0])

        if target is None:
            return "Usage: analyze [IP]"

        player.challenge_target = target.ip
        player.challenge_firewall = self.get_firewall_level(target)
        player.challenge = random.randint(5, 7)
        player.challenge_type = "analyzing"

        return (
            f"ANALYSIS STARTED: {target.ip}\n"
            f"TARGET FIREWALL: {player.challenge_firewall}\n"
            f"Analysis duration: {player.challenge} seconds."
        )

    def exploit(self, player, args):
        target = self.find_target(args[0]) if args else self.get_current_target(player)
        if target is None:
            return "Usage: exploit [IP]"

        firewall_level = self.get_firewall_level(target)
        exploit_level = self.exploit_power(player, target)

        if exploit_level < firewall_level:
            return (
                "EXPLOIT FAILED: FIREWALL TOO STRONG\n"
                f"YOUR EXPLOIT: {exploit_level}\n"
                f"TARGET FIREWALL: {firewall_level}"
            )

        player.challenge_target = target.ip
        player.challenge_type = "ready"
        player.challenge_firewall = firewall_level
        return f"EXPLOIT READY FOR {target.ip}. Run hack [amount]."

    def bypass(self, player, args):
        target = self.find_target(args[0]) if args else self.get_current_target(player)
        if target is None:
            return "Usage: bypass [IP]"

        firewall_level = self.get_firewall_level(target)
        if self.exploit_power(player, target) < firewall_level:
            return "BYPASS FAILED: EXPLOIT LEVEL TOO LOW."

        player.challenge_target = target.ip
        player.challenge_type = "ready"
        player.challenge_firewall = firewall_level
        return f"BYPASS SUCCESSFUL: {target.ip}"

    def inject(self, player, args):
        target = self.find_target(args[0]) if args else self.get_current_target(player)
        if target is None:
            return "Usage: inject [IP]"

        firewall_level = self.get_firewall_level(target)
        if self.exploit_power(player, target) < firewall_level:
            return "INJECTION FAILED: FIREWALL BLOCKED ACCESS."

        player.challenge_target = target.ip
        player.challenge_type = "ready"
        player.challenge_firewall = firewall_level
        return f"INJECTION READY: {target.ip}. Run hack [amount]."

    def hack(self, player, args, team_mode=False):
        self.last_hacked_player = None
        self.last_hack_stolen = 0
        self.last_hack_helpers = []

        if not player.challenge_target or player.challenge_type != "ready":
            return "ACCESS DENIED. Run analyze and complete it first."

        target = self.find_target(player.challenge_target)
        if target is None:
            return "TARGET LOST."

        if self.same_team(player, target):
            return "ACCESS DENIED: TEAMMATE NODE. YOU CANNOT ATTACK YOUR OWN TEAM."
        if getattr(target, "is_sub", False) and player.team is target.team:
            return "ACCESS DENIED: THIS IS YOUR OWN TEAM'S SUB MAINFRAME."

        helpers = self.team_helpers(player, target)
        if team_mode:
            team = player.team
            if team is None or len(team.members) < 2:
                return "TEAM HACK REQUIRES A TEAM OF 2 OR MORE. Use: team create duo"
            if not helpers:
                return (
                    "TEAM HACK NEEDS A TEAMMATE CONNECTED TO THE SAME TARGET.\n"
                    f"Ask a teammate to run: connect {target.ip}"
                )
        else:
            solo_helpers = helpers
            helpers = []

        firewall_level = self.get_firewall_level(target)
        power = player.economy.exploit_level + len(helpers)
        if power < firewall_level:
            if team_mode:
                return (
                    f"TEAM HACK FAILED: TEAM EXPLOIT POWER {power} "
                    f"IS BELOW FIREWALL {firewall_level}."
                )
            if solo_helpers:
                return (
                    "HACK FAILED: YOUR EXPLOIT LEVEL IS TOO LOW.\n"
                    "Use teamhack to combine your team's exploit power."
                )
            return "HACK FAILED: YOUR EXPLOIT LEVEL IS TOO LOW."

        participants = 1 + len(helpers)

        if isinstance(target, Player):
            if target.player_id == player.player_id:
                return "You cannot hack yourself."

            try:
                amount = int(args[0]) if args else 100
            except (ValueError, TypeError):
                return "Usage: hack [coin amount]"

            amount = min(max(1, amount), target.economy.coins)
            if amount <= 0:
                return "TARGET HAS NO COINS TO STEAL."

            target.economy.coins -= amount
            share = amount // participants
            player.economy.coins += amount - share * (participants - 1)
            for helper in helpers:
                helper.economy.coins += share
                helper.reputation += 10

            target.hacked = True
            target.attacker = None  # Never expose attacker ID on victim state.

            player.hacks_done += 1
            player.reputation += 25

            self.last_hacked_player = target.player_id
            self.last_hack_stolen = amount
            self.last_hack_helpers = [helper.player_id for helper in helpers]

            # Server-side record for traceback. The victim-facing event
            # should remain generic; only traceback should reveal identity.
            self.attack_records.append({
                "victim_id": target.player_id,
                "attacker_id": player.player_id,
                "attacker_name": player.name,
                "attacker_ip": player.ip,
                "disguised": bool(player.disguised),
                "timestamp": __import__("time").time(),
            })

            player.challenge_type = None
            player.challenge = None

            text = (
                "HACK SUCCESSFUL\n"
                f"TARGET: {target.ip}\n"
                f"COINS STOLEN: {amount}\n"
                f"YOUR COINS: {player.economy.coins}"
            )
            if helpers:
                text += f"\nTEAM SPLIT: {share} COINS EACH ({participants} MEMBERS)"
            return text

        if getattr(target, "is_sub", False):
            team = target.team
            if player.team is team:
                return "ACCESS DENIED: THIS IS YOUR OWN TEAM'S SUB MAINFRAME."
            if team.breach_remaining() > 0:
                return (
                    "SUB MAINFRAME ALREADY BREACHED.\n"
                    f"TEAM SHIELD DOWN FOR {team.breach_remaining():.0f} MORE SECONDS."
                )
            team.breached_until = time.time() + TEAM_SUB_BREACH_SECONDS
            self.last_hack_helpers = [helper.player_id for helper in helpers]
            player.challenge_type = None
            player.challenge = None
            return (
                "SUB MAINFRAME BREACHED\n"
                f"TARGET: {target.name}\n"
                f"TEAM SHIELD DOWN FOR {TEAM_SUB_BREACH_SECONDS} SECONDS.\n"
                "No coins are stored in a sub mainframe. Hit the team's player nodes now."
            )

        target.hacked = True
        target.attacker = player.player_id
        reward = 250 * max(1, firewall_level)

        share = reward // participants
        player.economy.coins += reward - share * (participants - 1)
        for helper in helpers:
            helper.economy.coins += share
            helper.reputation += 10
        player.hacks_done += 1
        player.reputation += 25
        self.last_hack_helpers = [helper.player_id for helper in helpers]

        player.challenge_type = None
        player.challenge = None

        text = (
            "SYSTEM COMPROMISED\n"
            f"TARGET: {target.name}\n"
            f"REWARD: {reward} coins\n"
            f"YOUR COINS: {player.economy.coins}"
        )
        if helpers:
            text += f"\nTEAM SPLIT: {share} COINS EACH ({participants} MEMBERS)"
        return text

    def traceback(self, player):
        # Only investigate attacks against this player.
        records = [
            record for record in self.attack_records
            if record["victim_id"] == player.player_id
        ]

        if not records:
            return "TRACEBACK FAILED: NO ATTACK TRACE FOUND."

        if not player.economy.has_item("traceback_tool"):
            return "TRACEBACK TOOL REQUIRED. Buy one from the black market."

        record = records[-1]

        # A disguise conceals identity even when the trace succeeds.
        if record.get("disguised"):
            player.economy.consume_item("traceback_tool")
            player.reputation += 5
            return (
                "TRACEBACK PARTIALLY SUCCESSFUL\n"
                f"ATTACKER IP: {record['attacker_ip']}\n"
                "IDENTITY: MASKED"
            )

        player.economy.consume_item("traceback_tool")
        player.reputation += 10

        attacker = self.find_player(record["attacker_id"])
        if attacker is None:
            return "TRACE FOUND, BUT THE ATTACKER HAS LEFT THE ROOM."

        return (
            "TRACEBACK SUCCESSFUL\n"
            f"ATTACKER: {record['attacker_name']}\n"
            f"ATTACKER IP: {record['attacker_ip']}\n"
            f"RANK: {attacker.get_rank()}"
        )

    def buy(self, player, args):
        if not args:
            return self.store(player)

        item = args[0].strip().lower()
        if item in ("ddos", "mitm"):
            attr = "ddos_owned" if item == "ddos" else "mitm_owned"
            if getattr(player, attr, False):
                return f"{item.upper()} ALREADY OWNED. OWNERSHIP IS PERMANENT."
            if player.economy.coins < 2500:
                return f"NOT ENOUGH COINS. {item.upper()} COSTS 2500 COINS."
            player.economy.coins -= 2500
            setattr(player, attr, True)
            return f"PURCHASE COMPLETE: {item.upper()} | -2500 COINS | PERMANENT OWNERSHIP."

        if item in BLACK_MARKET:
            result = player.economy.buy(item)
            if result.startswith("PURCHASE COMPLETE"):
                if item == "disguise":
                    player.disguised = True
                    player.disguise_name = f"UNKNOWN-{random.randint(100, 999)}"
            return result

        return player.economy.buy(item)

    def store(self, player):
        lines = [
            "CYBER//NET STORE",
            "----------------",
            "BLACK MARKET:",
        ]
        for item, price in BLACK_MARKET.items():
            lines.append(f"{item}: {price} coins")

        lines.extend([
            "",
            "PERMANENT ITEMS:",
            f"ddos: 2500 coins | {'OWNED' if getattr(player, 'ddos_owned', False) else 'NOT OWNED'}",
            f"mitm: 2500 coins | {'OWNED' if getattr(player, 'mitm_owned', False) else 'NOT OWNED'}",
            "",
            "Use: buy [item]",
            f"YOUR COINS: {player.economy.coins}",
        ])
        return "\n".join(lines)

    def ddos(self, player, args):
        if not getattr(player, "ddos_owned", False): return "DDoS NOT OWNED. Buy it from the Store for 2500 coins."
        if not args: return "Usage: ddos [target IP]"
        now = time.time()
        if now < getattr(player, "ddos_cooldown_until", 0): return f"DDoS COOLDOWN. WAIT {player.ddos_cooldown_until-now:.1f} SECONDS."
        target = self.find_target(args[0])
        if target is None or target is player: return "INVALID TARGET. Choose another simulated network node."
        if self.same_team(player, target): return "DDoS BLOCKED: TEAMMATE NODE."
        target.ddos_disabled_until = now + 20
        player.ddos_cooldown_until = now + 45
        return f"SIMULATED DDoS SUCCESSFUL: {target.ip}. FIREWALL WEAKENED FOR 20 SECONDS."

    def mitm(self, player, args):
        if not getattr(player, "mitm_owned", False): return "MitM NOT OWNED. Buy it from the Store for 2500 coins."
        if not args: return "Usage: mitm [player IP]"
        now = time.time()
        if now < getattr(player, "mitm_cooldown_until", 0): return f"MitM COOLDOWN. WAIT {player.mitm_cooldown_until-now:.1f} SECONDS."
        target = self.find_target(args[0])
        if not isinstance(target, Player) or target.player_id == player.player_id: return "MitM TARGET MUST BE ANOTHER PLAYER NODE."
        if self.same_team(player, target): return "MitM BLOCKED: TEAMMATE NODE."
        stolen = max(0, int(target.economy.coins) // 2)
        if stolen <= 0: return "MitM FAILED: TARGET HAS NO COINS TO INTERCEPT."
        target.economy.coins -= stolen
        player.economy.coins += stolen
        player.mitm_cooldown_until = now + 30
        player.reputation += 10
        return "SIMULATED MitM SUCCESSFUL: userdata.dat intercepted.\nCOINS INTERCEPTED: %s (50%% of target balance)\nNo real files or networks were accessed." % stolen

    def hardware(self, player):
        return ("HARDWARE / MOTHERBOARD\n----------------------\n"
                f"CPU: TIER {getattr(player, 'cpu_level', 1)} (faster analysis)\n"
                f"RAM: TIER {getattr(player, 'ram_level', 1)} ({4*getattr(player, 'ram_level', 1)} GB simulated)\n"
                f"GPU: {getattr(player, 'gpu_count', 0)} installed (mining)\n"
                f"STORAGE: TIER {getattr(player, 'storage_level', 1)} ({100*getattr(player, 'storage_level', 1)} GB simulated)\n"
                "Upgrade with: upgrade [cpu|ram|storage]. Buy GPUs with the BITCOIN panel.")

    def inventory(self, player):
        text = player.economy.inventory_text()
        owned = [name for name, attr in (("DDoS (PERMANENT)", "ddos_owned"), ("MitM (PERMANENT)", "mitm_owned")) if getattr(player, attr, False)]
        return text + ("\n" + "\n".join(owned) if owned else "")

    # -----------------------------------------------------------------
    # TEAM COMMANDS
    # -----------------------------------------------------------------

    def find_team_by_name(self, name):
        name = str(name).strip().upper()
        for team in self.teams.values():
            if team.name == name:
                return team
        return None

    def team_command(self, player, args):
        if not args:
            return self.team_status(player)

        action = args[0].lower()
        rest = args[1:]

        if action in ("status", "info"):
            return self.team_status(player)
        if action == "list":
            return self.team_list()
        if action == "create":
            return self.team_create(player, rest)
        if action == "join":
            return self.team_join(player, rest)
        if action == "leave":
            return self.team_leave(player)
        if action == "kick":
            return self.team_kick(player, rest)
        if action == "sub":
            return self.team_buy_sub(player)
        return TEAM_USAGE

    def team_status(self, player):
        team = player.team
        if team is None:
            return "YOU ARE NOT IN A TEAM.\n\n" + TEAM_USAGE

        lines = [
            f"TEAM: {team.name} ({team.team_type.upper()})",
            f"MEMBERS ({len(team.members)}/{team.max_members}):",
        ]
        for member in team.members:
            lines.append(f"- {member.name}" + (" (LEADER)" if member is team.leader else ""))

        if team.sub is None:
            lines.append(f"SUB MAINFRAME: NOT BUILT (leader: team sub, {TEAM_SUB_PRICE} coins)")
        else:
            lines.append(f"SUB MAINFRAME: {team.sub.name} | {team.sub.ip}")
            if team.shield_active():
                lines.append(f"TEAM FIREWALL: {team.firewall_level()} (SHIELD ACTIVE)")
            else:
                lines.append(f"TEAM FIREWALL: DOWN FOR {team.breach_remaining():.0f} SECONDS (BREACHED)")
        return "\n".join(lines)

    def team_list(self):
        if not self.teams:
            return "NO TEAMS YET. Create one with: team create duo"
        lines = ["TEAMS", "-----"]
        for team in self.teams.values():
            sub = team.sub.ip if team.sub else "NO SUB"
            lines.append(
                f"{team.name} | {team.team_type.upper()} | "
                f"{len(team.members)}/{team.max_members} | {sub}"
            )
        return "\n".join(lines)

    def team_create(self, player, rest):
        if player.team is not None:
            return f"ALREADY IN TEAM {player.team.name}. Use: team leave"
        if not rest or rest[0].lower() not in TEAM_TYPES:
            return "Usage: team create [duo|trio|quadro] [name]"

        team_type = rest[0].lower()
        name = ""
        if len(rest) > 1:
            name = "".join(c for c in rest[1].upper() if c.isalnum() or c in "_-")[:12]
            if len(name) < 2:
                return "TEAM NAME MUST BE 2-12 LETTERS, NUMBERS, _ OR -."
        else:
            for candidate in DEFAULT_TEAM_NAMES:
                if self.find_team_by_name(candidate) is None:
                    name = candidate
                    break
            if not name:
                name = f"TEAM-{self.team_counter + 1}"

        if self.find_team_by_name(name) is not None:
            return "TEAM NAME ALREADY TAKEN."

        self.team_counter += 1
        team = Team(self.team_counter, name, team_type, player)
        self.teams[team.team_id] = team
        player.team = team
        return (
            f"TEAM {name} CREATED ({team_type.upper()}, UP TO {team.max_members} MEMBERS).\n"
            f"Others can join with: team join {name}\n"
            f"Leader can build the SUB MAINFRAME for {TEAM_SUB_PRICE} coins: team sub"
        )

    def team_join(self, player, rest):
        if player.team is not None:
            return f"ALREADY IN TEAM {player.team.name}. Use: team leave"
        if not rest:
            return "Usage: team join [name]"
        team = self.find_team_by_name(rest[0])
        if team is None:
            return "TEAM NOT FOUND. Use: team list"
        if len(team.members) >= team.max_members:
            return "TEAM IS FULL."
        team.members.append(player)
        player.team = team
        return f"JOINED TEAM {team.name} ({len(team.members)}/{team.max_members})."

    def remove_from_team(self, player):
        """Remove a player from their team. Returns True if the team was disbanded."""
        team = player.team
        if team is None:
            return False
        if player in team.members:
            team.members.remove(player)
        player.team = None
        if not team.members:
            self.remove_sub(team)
            self.teams.pop(team.team_id, None)
            return True
        if team.leader is player:
            team.leader = team.members[0]
        return False

    def remove_sub(self, team):
        sub = team.sub
        if sub is None:
            return
        self.computers.pop(sub.ip, None)
        for other in self.players.values():
            if getattr(other, "current_ip", None) == sub.ip:
                other.current_ip = "10.0.0.99"
            if getattr(other, "challenge_target", None) == sub.ip:
                other.challenge = None
                other.challenge_type = None
                other.challenge_target = None
                other.challenge_firewall = None
        team.sub = None

    def team_leave(self, player):
        team = player.team
        if team is None:
            return "YOU ARE NOT IN A TEAM."
        disbanded = self.remove_from_team(player)
        text = f"YOU LEFT TEAM {team.name}."
        if disbanded:
            text += " THE TEAM WAS DISBANDED."
        return text

    def team_kick(self, player, rest):
        team = player.team
        if team is None:
            return "YOU ARE NOT IN A TEAM."
        if team.leader is not player:
            return "ONLY THE TEAM LEADER CAN KICK MEMBERS."
        if not rest:
            return "Usage: team kick [player name]"
        wanted = rest[0].lower()
        for member in list(team.members):
            if member is not player and member.name.lower() == wanted:
                self.remove_from_team(member)
                return f"{member.name} WAS REMOVED FROM TEAM {team.name}."
        return "NO SUCH TEAMMATE."

    def team_buy_sub(self, player):
        team = player.team
        if team is None:
            return "YOU ARE NOT IN A TEAM."
        if team.leader is not player:
            return "ONLY THE TEAM LEADER CAN BUY THE SUB MAINFRAME."
        if team.sub is not None:
            return "SUB MAINFRAME ALREADY BUILT."
        if player.economy.coins < TEAM_SUB_PRICE:
            return f"NOT ENOUGH COINS. SUB MAINFRAME COSTS {TEAM_SUB_PRICE} COINS."

        while True:
            ip = f"10.0.1.{random.randint(10, 250)}"
            if ip not in self.computers:
                break

        player.economy.coins -= TEAM_SUB_PRICE
        team.sub = SubMainframe(team, ip)
        self.computers[ip] = team.sub
        return (
            "SUB MAINFRAME BUILT\n"
            f"NAME: {team.sub.name}\n"
            f"IP: {ip}\n"
            f"TEAM FIREWALL: {team.firewall_level()} (protects every teammate)\n"
            f"COST: {TEAM_SUB_PRICE} | COINS LEFT: {player.economy.coins}"
        )

    def status(self, player):
        return (
            f"PLAYER: {player.name}\n"
            f"IP: {player.ip}\n"
            f"COINS: {player.economy.coins}\n"
            f"EXPLOIT LEVEL: {player.economy.exploit_level}\n"
            f"FIREWALL LEVEL: {player.economy.firewall_level}\n"
            f"HACKS: {player.hacks_done}\n"
            f"REPUTATION: {player.reputation}\n"
            f"RANK: {player.get_rank()}\n"
            f"DETECTION: {player.detection}"
            + (f"\nTEAM: {player.team.name} ({player.team.team_type.upper()})" if player.team else "")
        )

    def players_info(self):
        if not self.players:
            return "NO PLAYERS CONNECTED."

        lines = ["CONNECTED PLAYERS", "------------------"]
        for player in self.players.values():
            lines.append(
                f"{player.name} | {player.ip} | "
                f"{player.get_rank()} | {player.hacks_done} hacks"
            )
        return "\n".join(lines)

    def files_info(self, player):
        target = self.get_current_target(player)
        if not isinstance(target, Computer):
            return "Connect to a computer first."
        return "FILES:\n" + "\n".join(target.files.keys())

    def read_file(self, player, args):
        if not args:
            return "Usage: read [filename]"

        target = self.get_current_target(player)
        if not isinstance(target, Computer):
            return "Connect to a computer first."

        filename = args[0]
        if filename not in target.files:
            return "FILE NOT FOUND."

        return f"{filename}\n----------------\n{target.files[filename]}"

    def help_text(self):
        return (
            "CYBER//NET COMMANDS\n"
            "help, tutorial, scan, connect [IP], disconnect,\n"
            "info [IP], ports [IP], probe [IP], analyze [IP],\n"
            "exploit [IP], bypass [IP], inject [IP], hack [amount],\n"
            "files, read [filename], status, players, store,\n"
            "inventory, buy [item], upgrade [speed|firewall|exploit|cpu|ram|storage],\n"
            "hardware, ddos [IP], mitm [player IP], traceback,\n"
            "team [create|join|leave|kick|list|sub], teamhack [amount]"
        )

    def tutorial(self):
        return (
            "CYBER//NET TUTORIAL\n"
            "1. Use scan to discover network nodes.\n"
            "2. Connect to a target IP.\n"
            "3. Analyze the target and complete the analysis.\n"
            "4. Use exploit or bypass if your level is high enough.\n"
            "5. Run hack to attempt the attack.\n"
            "6. Buy a traceback_tool to investigate attacks against you.\n"
            "7. Earn reputation to climb the ranks."
        )

    def command(self, player, command):
        self.last_hacked_player = None
        self.last_hack_stolen = 0
        self.last_hack_helpers = []

        if not isinstance(command, str):
            return "INVALID COMMAND."

        command = command.strip()
        if not command:
            return ""

        parts = command.split()
        name = parts[0].lower().rstrip(":")
        args = parts[1:]

        handlers = {
            "help": lambda: self.help_text(),
            "tutorial": lambda: self.tutorial(),
            "scan": lambda: self.scan(player),
            "connect": lambda: self.connect(player, args),
            "disconnect": lambda: self.disconnect(player),
            "info": lambda: self.info(player, args),
            "ports": lambda: self.ports(player, args),
            "probe": lambda: self.probe(player, args),
            "analyze": lambda: self.analyze(player, args),
            "exploit": lambda: self.exploit(player, args),
            "bypass": lambda: self.bypass(player, args),
            "inject": lambda: self.inject(player, args),
            "hack": lambda: self.hack(player, args),
            "teamhack": lambda: self.hack(player, args, team_mode=True),
            "team": lambda: self.team_command(player, args),
            "files": lambda: self.files_info(player),
            "read": lambda: self.read_file(player, args),
            "status": lambda: self.status(player),
            "players": lambda: self.players_info(),
            "store": lambda: self.store(player),
            "inventory": lambda: self.inventory(player),
            "buy": lambda: self.buy(player, args),
            "upgrade": lambda: self.upgrade(player, args[0]) if args
            else "Usage: upgrade [speed|firewall|exploit]",
            "traceback": lambda: self.traceback(player),
            "ddos": lambda: self.ddos(player, args),
            "mitm": lambda: self.mitm(player, args),
            "hardware": lambda: self.hardware(player),
        }

        if name not in handlers:
            return f"UNKNOWN COMMAND: {name}. Type help."

        try:
            return handlers[name]()
        except Exception as exc:
            return f"COMMAND ERROR: {type(exc).__name__}: {exc}"