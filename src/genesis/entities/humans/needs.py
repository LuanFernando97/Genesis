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

    @staticmethod
    def _clamp(value: int) -> int:
        return max(0, min(100, value))

    def _increase(self, attribute: str, amount: int) -> None:
        current_value = getattr(self, attribute)
        new_value = Needs._clamp(current_value + amount)
        setattr(self, attribute, new_value)

    def _decrease(self, attribute: str, amount: int) -> None:
        current_value = getattr(self, attribute)
        new_value = Needs._clamp(current_value - amount)
        setattr(self, attribute, new_value)

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

    def increase_energy(self, amount: int) -> None:
        self._increase("_energy", amount)

    def decrease_energy(self, amount: int) -> None:
        self._decrease("_energy", amount)

    def increase_hunger(self, amount: int) -> None:
        self._increase("_hunger", amount)

    def decrease_hunger(self, amount: int) -> None:
        self._decrease("_hunger", amount)

    def increase_thirst(self, amount: int) -> None:
        self._increase("_thirst", amount)

    def decrease_thirst(self, amount: int) -> None:
        self._decrease("_thirst", amount)

    def increase_health(self, amount: int) -> None:
        self._increase("_health", amount)

    def decrease_health(self, amount: int) -> None:
        self._decrease("_health", amount)
