import pytest

from genesis.infrastructure.position import Position
from genesis.world.terrain import TerrainType
from genesis.world.world_generator import WorldGenerator


def test_generate_world_creates_world():
    generator = WorldGenerator(seed=123)

    world = generator.generate(
        width=10,
        height=10,
    )

    assert world.width == 10
    assert world.height == 10
    assert world.seed == 123


def test_generator_accepts_none_seed():
    generator = WorldGenerator()

    assert generator.seed is not None


def test_generator_accepts_integer_seed():
    generator = WorldGenerator(123)

    assert generator.seed == 123


def test_generator_rejects_negative_seed():
    with pytest.raises(ValueError):
        WorldGenerator(-1)


def test_generator_rejects_invalid_seed_type():
    with pytest.raises(TypeError):
        WorldGenerator("123")


def test_generate_world_creates_grid():
    generator = WorldGenerator(seed=123)

    world = generator.generate(
        width=10,
        height=10,
    )

    assert world.grid is not None


def test_generate_world_creates_tiles():
    generator = WorldGenerator(seed=123)

    world = generator.generate(
        width=10,
        height=10,
    )

    tile = world.grid.get(Position(5, 5))

    assert tile is not None
    assert tile.position == Position(5, 5)


def test_generate_world_creates_terrain():
    generator = WorldGenerator(seed=123)

    world = generator.generate(
        width=10,
        height=10,
    )

    tile = world.grid.get(Position(5, 5))

    assert tile.terrain in TerrainType


def test_generate_world_creates_resources():
    generator = WorldGenerator(seed=123)

    world = generator.generate(
        width=20,
        height=20,
    )

    has_resources = False

    for y in range(20):
        for x in range(20):
            tile = world.grid.get(Position(x, y))

            if len(tile.resources) > 0:
                has_resources = True

    assert has_resources


def test_same_seed_generates_same_world():
    generator_a = WorldGenerator(seed=123)
    generator_b = WorldGenerator(seed=123)

    world_a = generator_a.generate(20, 20)
    world_b = generator_b.generate(20, 20)

    for y in range(20):
        for x in range(20):
            position = Position(x, y)

            tile_a = world_a.grid.get(position)
            tile_b = world_b.grid.get(position)

            assert tile_a.terrain == tile_b.terrain
            assert tile_a.resources == tile_b.resources


def test_different_seed_generates_different_world():
    generator_a = WorldGenerator(seed=123)
    generator_b = WorldGenerator(seed=456)

    world_a = generator_a.generate(20, 20)
    world_b = generator_b.generate(20, 20)

    different = False

    for y in range(20):
        for x in range(20):
            position = Position(x, y)

            tile_a = world_a.grid.get(position)
            tile_b = world_b.grid.get(position)

            if tile_a.terrain != tile_b.terrain:
                different = True
                break

    assert different
