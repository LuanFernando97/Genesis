from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterator, Self

from genesis.entities.id_generator import EntityIdGenerator
from genesis.entities.registry import EntityRegistry
from genesis.infrastructure.logger import get_logger

ENTITY_LOGGER_LEVEL = "debug"


class Entity(ABC):
    _entity_id_generator: EntityIdGenerator = EntityIdGenerator()
    _registry: EntityRegistry = EntityRegistry()
    logger = get_logger("entity", level=ENTITY_LOGGER_LEVEL)

    def __init__(self) -> None:
        self._alive = True
        self.id, self.display_id = self._generate_ids()

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

    def spawn(self) -> None:
        self._registry.add(self)

    def despawn(self) -> None:
        if not self._alive:
            return

        self._registry.remove(self)

        self._alive = False

    @abstractmethod
    def update(self) -> None:
        Entity.logger.debug(self)

    def __repr__(self) -> str:
        return f"<Entity={self.__class__.__name__} id={self.display_id}>"
