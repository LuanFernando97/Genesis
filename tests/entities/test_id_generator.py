from genesis.entities.id_generator import EntityIdGenerator


class FakeEntity:
    pass


class FakeEntity2:
    pass


def test_generate_unique_uuid():
    generator = EntityIdGenerator()

    uuid_1, _ = generator.generate(FakeEntity)
    uuid_2, _ = generator.generate(FakeEntity)

    assert isinstance(uuid_1, str)
    assert isinstance(uuid_2, str)

    assert uuid_1 != uuid_2


def test_display_id_is_incremental_per_entity_type():
    generator = EntityIdGenerator()

    _, fake_entity_1 = generator.generate(FakeEntity)
    _, fake_entity_2 = generator.generate(FakeEntity)

    _, fake_entity2_2 = generator.generate(FakeEntity2)

    assert fake_entity_1 == 1
    assert fake_entity_2 == 2
    assert fake_entity2_2 == 1


def test_display_id_is_not_reused():
    generator = EntityIdGenerator()

    _, first_id = generator.generate(FakeEntity)
    _, second_id = generator.generate(FakeEntity)

    assert first_id == 1
    assert second_id == 2
