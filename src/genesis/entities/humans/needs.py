class Needs:
    def __init__(
        self,
        energy: int = 100,
        hunger: int = 0,
        thirst: int = 0,
        health: int = 100,
    ) -> None:
        self._energy = self._validate(energy)
        self._hunger = self._validate(hunger)
        self._thirst = self._validate(thirst)
        self._health = self._validate(health)

    @staticmethod
    def _validate(value: int) -> int:
        if not 0 <= value <= 100:
            raise ValueError("Need values must be between 0 and 100.")
        return value

    @property
    def energy(self) -> int:
        return self._energy

    @property
    def hunger(self) -> int:
        return self._hunger

    @property
    def thirst(self) -> int:
        return self._thirst

    @property
    def health(self) -> int:
        return self._health
