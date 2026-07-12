class Clock:
    def __init__(self):
        self._ticks = 0

    def tick(self):
        self._ticks += 1

    @property
    def current_tick(self):
        return self._ticks

    def reset(self):
        self._ticks = 0

    def advance(self, amount):
        self._ticks += amount

    def __repr__(self):
        return f"<Clock current_tick={self.current_tick}>"
