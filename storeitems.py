
# =========================================================
# CYBER//NET - STORE ITEMS
# =========================================================

STORE_ITEMS = {
    "speed": {
        "name": "2X SPEED",
        "base_price": 500,
        "description": "Makes target analysis faster."
    },

    "firewall": {
        "name": "FIREWALL +1",
        "base_price": 750,
        "description": "Increases your fictional firewall level by 1."
    },

    "exploit": {
        "name": "EXPLOIT +1",
        "base_price": 750,
        "description": "Increases your fictional exploit level by 1."
    }
}


def get_item(item_id):
    return STORE_ITEMS.get(item_id)


def get_item_price(item_id, level=0):
    item = get_item(item_id)

    if item is None:
        return None

    level = max(0, int(level))
    return item["base_price"] * (2 ** level)


def get_store_items():
    return STORE_ITEMS.copy()


def format_store(player):
    speed_level = getattr(player, "speed_upgrade_level", 0)
    firewall_level = getattr(player, "firewall_upgrade_level", 0)
    exploit_level = getattr(player, "exploit_upgrade_level", 0)

    speed_price = get_item_price("speed", speed_level)
    firewall_price = get_item_price("firewall", firewall_level)
    exploit_price = get_item_price("exploit", exploit_level)

    lines = [
        "========================================",
        "              CYBER//NET STORE",
        "========================================",
        "",
        f"2X SPEED          {speed_price} coins",
        f"FIREWALL +1       {firewall_price} coins",
        f"EXPLOIT +1        {exploit_price} coins",
        "",
        "========================================",
        "Use:",
        "upgrade speed",
        "upgrade firewall",
        "upgrade exploit",
        "========================================"
    ]

    return "\n".join(lines)


def get_upgrade_price(upgrade_type, player):
    levels = {
        "speed": getattr(player, "speed_upgrade_level", 0),
        "firewall": getattr(player, "firewall_upgrade_level", 0),
        "exploit": getattr(player, "exploit_upgrade_level", 0)
    }

    if upgrade_type not in levels:
        return None

    return get_item_price(upgrade_type, levels[upgrade_type])
