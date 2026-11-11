
class PlayerEconomy:
    STARTING_COINS = 500

    # Existing shop + new black-market items.
    PRICES = {
        "exploit_kit": 100,
        "firewall_01": 150,
        "trace_mask": 200,

        "disguise": 300,
        "ip_reroll": 200,
        "firewall_patch": 250,
        "counter_hack": 350,
        "traceback_tool": 300,
    }

    def __init__(self):
        self.coins = self.STARTING_COINS
        self.exploit_level = 1
        self.firewall_level = 1
        self.inventory = []

    def inventory_text(self):
        items = [
            f"Coins: {self.coins}",
            f"Exploit Level: {self.exploit_level}",
            f"Firewall Level: {self.firewall_level}",
        ]

        items.append("")
        items.append("ITEMS:")

        if self.inventory:
            for item in self.inventory:
                items.append(f"- {item}")
        else:
            items.append("- none")

        return "\n".join(items)

    def buy(self, item):
        item = str(item).strip().lower()

        if item not in self.PRICES:
            return "Item not found."

        price = self.PRICES[item]

        if self.coins < price:
            return "Not enough coins."

        self.coins -= price

        if item == "exploit_kit":
            self.exploit_level += 1

        elif item == "firewall_01":
            self.firewall_level += 1

        # Black-market items are stored in inventory.
        # Their effects must be validated and applied by
        # the server/game code, never by the browser.
        self.inventory.append(item)

        return (
            "PURCHASE COMPLETE\n"
            "-----------------\n"
            f"ITEM: {item}\n"
            f"COST: {price}\n"
            f"COINS LEFT: {self.coins}"
        )

    def has_item(self, item):
        return str(item).strip().lower() in self.inventory

    def consume_item(self, item):
        item = str(item).strip().lower()

        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return True

    def to_dict(self):
        """Return account progress in a JSON/SQLite-friendly format."""
        return {
            "coins": int(self.coins),
            "exploit_level": int(self.exploit_level),
            "firewall_level": int(self.firewall_level),
            "inventory": list(self.inventory),
        }

    def load_dict(self, data):
        """Restore saved progress without replacing missing defaults."""
        if not isinstance(data, dict):
            return

        try:
            self.coins = max(0, int(data.get("coins", self.STARTING_COINS)))
            self.exploit_level = max(1, int(data.get("exploit_level", 1)))
            self.firewall_level = max(1, int(data.get("firewall_level", 1)))

            inventory = data.get("inventory", [])
            if isinstance(inventory, list):
                self.inventory = [
                    str(item).strip().lower()
                    for item in inventory
                    if isinstance(item, str)
                    and str(item).strip().lower() in self.PRICES
                ]
        except (TypeError, ValueError):
            # Ignore malformed saved fields rather than crashing the game.
            return
