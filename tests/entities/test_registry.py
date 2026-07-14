from uuid import uuid4

from genesis.entities.registry import EntityRegistry


class FakeEntity:
    def __init__(self) -> None:
        self.id = uuid4()


class FakeEntity2:
    def __init__(self) -> None:
        self.id = uuid4()


def test_registry_add_entity():
    registry = EntityRegistry()
    entity = FakeEntity()

    registry.add(entity)

    assert len(registry) == 1
    assert registry.get(entity.id) == entity


def test_registry_remove_entity():
    registry = EntityRegistry()
    entity = FakeEntity()

    registry.add(entity)
    registry.remove(entity)

    assert len(registry) == 0
    assert registry.get(entity.id) is None


def test_registry_get_unknown_entity_returns_none():
    registry = EntityRegistry()

    entity = registry.get(uuid4())

    assert entity is None


def test_registry_handles_different_entity_types():
    registry = EntityRegistry()

    entity_1 = FakeEntity()
    entity_2 = FakeEntity2()

    registry.add(entity_1)
    registry.add(entity_2)

    assert len(registry) == 2
    assert registry.get(entity_1.id) == entity_1
    assert registry.get(entity_2.id) == entity_2


def test_registry_iterates_entities():
    registry = EntityRegistry()

    entity_1 = FakeEntity()
    entity_2 = FakeEntity2()

    registry.add(entity_1)
    registry.add(entity_2)

    entities = list(registry)

    assert entity_1 in entities
    assert entity_2 in entities
    assert len(entities) == 2


def test_registry_does_not_fail_when_removing_unknown_entity():
    registry = EntityRegistry()
    entity = FakeEntity()

    registry.remove(entity)

    assert len(registry) == 0
