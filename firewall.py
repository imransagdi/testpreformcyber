
class Firewall:

    def __init__(self, level=1):
        self.level = int(level)

    def check(self, exploit_level):
        return exploit_level >= self.level

    def description(self):
        return f"FIREWALL LEVEL {self.level}"

