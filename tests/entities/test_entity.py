from genesis.entities.entity import Entity


class FakeEntity(Entity):
    def update(self):
        pass


class FakeEntity2(Entity):
    def update(self):
        pass


def test_entity_spawn_creates_entity():
    entity = FakeEntity()
    entity.spawn()

    assert isinstance(entity, FakeEntity)


def test_entity_spawn_generates_unique_ids():
    entity_1 = FakeEntity()
    entity_2 = FakeEntity()
    entity_1.spawn()
    entity_2.spawn()

    assert entity_1.id != entity_2.id
    assert entity_1.display_id == 1
    assert entity_2.display_id == 2


def test_entities_registry_contains_spawned_entities():
    entity_1 = FakeEntity()
    entity_2 = FakeEntity2()
    entity_1.spawn()
    entity_2.spawn()

    entities = list(Entity.entities())

    assert entity_1 in entities
    assert entity_2 in entities
    assert len(entities) == 2


def test_entity_is_alive_after_spawn():
    entity = FakeEntity()
    entity.spawn()

    assert entity.is_alive is True


def test_entity_despawn_removes_entity_from_registry():
    entity = FakeEntity()
    entity.spawn()

    entity.despawn()

    entities = list(Entity.entities())

    assert entity not in entities
    assert entity.is_alive is False


def test_entity_despawn_is_idempotent():
    entity = FakeEntity()
    entity.spawn()

    entity.despawn()
    entity.despawn()

    assert entity.is_alive is False


def test_entity_repr_returns_class_name_and_display_id():
    entity = FakeEntity()
    entity.spawn()

    assert repr(entity) == "<Entity=FakeEntity id=1>"
