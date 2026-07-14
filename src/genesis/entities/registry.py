from __future__ import annotations

from typing import TYPE_CHECKING, Iterator

if TYPE_CHECKING:
    from genesis.entities.entity import Entity


class EntityRegistry:
    def __init__(self) -> None:
        self._entities: dict[str, Entity] = {}

    def add(self, entity: Entity) -> None:
        self._entities[entity.id] = entity

    def remove(self, entity: Entity) -> None:
        self._entities.pop(entity.id, None)

    def get(self, entity_id: str) -> Entity | None:
        return self._entities.get(entity_id)

    def __iter__(self) -> Iterator[Entity]:
        return iter(self._entities.values())

    def __len__(self) -> int:
        return len(self._entities)
