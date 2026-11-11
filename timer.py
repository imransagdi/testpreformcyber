
import time
import random


class GameTimer:

    def __init__(
        self,
        duration=None
    ):
        if duration is None:
            duration = random.uniform(
                5.0,
                7.0
            )

        self.duration = float(duration)
        self.started_at = time.time()
        self.finished = False

    @property
    def expires_at(self):
        return (
            self.started_at +
            self.duration
        )

    def remaining(self):
        if self.finished:
            return 0.0

        return max(
            0.0,
            self.expires_at -
            time.time()
        )

    def is_finished(self):
        if self.finished:
            return True

        if time.time() >= self.expires_at:
            self.finished = True
            return True

        return False

    def progress(self):
        if self.duration <= 0:
            return 1.0

        elapsed = (
            time.time() -
            self.started_at
        )

        return max(
            0.0,
            min(
                1.0,
                elapsed /
                self.duration
            )
        )

