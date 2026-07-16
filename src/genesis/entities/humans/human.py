from genesis.entities.entity import Entity
from genesis.simulation.simulation import Simulation

from .sex import Sex


class Human(Entity):
    def __init__(self, simulation: Simulation, name: str, sex: Sex, age: int) -> None:
        super().__init__(simulation)

        if not name:
            raise ValueError("Name cannot be empty.")

        if age < 0:
            raise ValueError("Age cannot be negative.")

        self._name = name
        self._sex = sex
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @property
    def sex(self) -> Sex:
        return self._sex

    @property
    def age(self) -> int:
        return self._age
