from genesis.entities.entity import Entity
from genesis.infrastructure.position import Position
from genesis.simulation.simulation import Simulation

from .needs import Needs
from .sex import Sex


class Human(Entity):
    def __init__(
        self,
        simulation: Simulation,
        name: str,
        sex: Sex,
        age: int,
        position: Position,
        needs: Needs | None = None,
    ) -> None:
        super().__init__(simulation)

        if not name:
            raise ValueError("Name cannot be empty.")

        if age < 0:
            raise ValueError("Age cannot be negative.")

        if not isinstance(position, Position):
            raise TypeError("position must be a Position.")

        self._name = name
        self._sex = sex
        self._age = age
        self._position = position
        self._needs = needs or Needs()

    @property
    def name(self) -> str:
        return self._name

    @property
    def sex(self) -> Sex:
        return self._sex

    @property
    def age(self) -> int:
        return self._age

    @property
    def needs(self) -> Needs:
        return self._needs

    @property
    def position(self) -> Position:
        return self._position

    @position.setter
    def position(self, position: Position) -> None:
        if not isinstance(position, Position):
            raise TypeError("position must be a Position.")

        self._position = position
