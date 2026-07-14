from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, Iterator, Self

from genesis.entities.id_generator import EntityIdGenerator
from genesis.entities.registry import EntityRegistry

if TYPE_CHECKING:
    from genesis.simulation.simulation import Simulation


class Entity(ABC):
    _entity_id_generator: EntityIdGenerator = EntityIdGenerator()
    _registry: EntityRegistry = EntityRegistry()

    def __init__(self, simulation: Simulation) -> None:
        self._simulation = simulation
        self._alive = True
        self.id, self.display_id = self._generate_ids()

    @property
    def simulation(self) -> Simulation:
        return self._simulation

    @property
    def is_alive(self) -> bool:
        return self._alive

    @staticmethod
    def _reset():
        Entity._registry = EntityRegistry()
        Entity._entity_id_generator = EntityIdGenerator()

    @classmethod
    def _generate_ids(cls) -> tuple[str, int]:
        return cls._entity_id_generator.generate(cls)

    @classmethod
    def entities(cls) -> Iterator[Self]:
        return iter(cls._registry)

    @classmethod
    def spawn(cls, simulation: Simulation) -> Self:
        entity = cls(simulation)

        cls._registry.add(entity)

        return entity

    def despawn(self) -> None:
        if not self._alive:
            return

        self._registry.remove(self)

        self._alive = False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}_{self.display_id}"
