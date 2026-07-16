from genesis.entities.entity import Entity


class FakeEntity(Entity):
    pass


class FakeEntity2(Entity):
    pass


class FakeSimulation:
    pass


def test_entity_spawn_creates_entity(simulation):
    entity = FakeEntity.spawn(simulation)

    assert isinstance(entity, FakeEntity)
    assert entity.simulation == simulation


def test_entity_spawn_generates_unique_ids(simulation):
    entity_1 = FakeEntity.spawn(simulation)
    entity_2 = FakeEntity.spawn(simulation)

    assert entity_1.id != entity_2.id
    assert entity_1.display_id == 1
    assert entity_2.display_id == 2


def test_entities_registry_contains_spawned_entities(simulation):
    entity_1 = FakeEntity.spawn(simulation)
    entity_2 = FakeEntity2.spawn(simulation)

    entities = list(Entity.entities())

    assert entity_1 in entities
    assert entity_2 in entities
    assert len(entities) == 2


def test_entity_is_alive_after_spawn(simulation):
    entity = FakeEntity.spawn(simulation)

    assert entity.is_alive is True


def test_entity_despawn_removes_entity_from_registry(simulation):
    entity = FakeEntity.spawn(simulation)

    entity.despawn()

    entities = list(Entity.entities())

    assert entity not in entities
    assert entity.is_alive is False


def test_entity_despawn_is_idempotent(simulation):
    entity = FakeEntity.spawn(simulation)

    entity.despawn()
    entity.despawn()

    assert entity.is_alive is False


def test_entity_repr_returns_class_name_and_display_id(simulation):
    entity = FakeEntity.spawn(simulation)

    assert repr(entity) == "FakeEntity_1"
