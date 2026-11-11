# =========================================================
# CYBER//NET - AUTOHACK
# =========================================================

class AutoHack:
    def __init__(self):
        self.level = 0
        self.enabled = False

    def unlock(self):
        if self.level < 1:
            self.level = 1

        self.enabled = True
        return True

    def upgrade(self):
        if self.level < 1:
            return False

        self.level += 1
        self.enabled = True
        return True

    def is_unlocked(self):
        return self.enabled and self.level >= 1

    def get_level(self):
        return self.level

    def get_status(self):
        if not self.is_unlocked():
            return "AUTOHACK: LOCKED"

        return f"AUTOHACK: LEVEL {self.level}"

    def get_analysis_delay(self, normal_delay):
        if not self.is_unlocked():
            return normal_delay

        if self.level == 1:
            return normal_delay

        return normal_delay / self.level


def create_autohack():
    return AutoHack()