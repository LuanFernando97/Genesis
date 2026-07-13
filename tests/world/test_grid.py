from genesis.infrastructure.position import Position
from genesis.world.grid import Grid


def test_create_empty_grid():
    grid = Grid(10, 10)

    assert grid.width == 10
    assert grid.height == 10


def test_position_exists():
    grid = Grid(10, 10)

    assert grid.contains(Position(5, 5))
    assert not grid.contains(Position(20, 5))


def test_get_empty_position():
    grid = Grid(10, 10)

    assert grid.get(Position(2, 2)) is None


def test_set_value():
    grid = Grid(10, 10)

    grid.set(Position(2, 2), "tile")

    assert grid.get(Position(2, 2)) == "tile"


def test_get_neighbors():
    grid = Grid(3, 3)

    neighbors = grid.neighbors(Position(1, 1))

    assert len(neighbors) == 8
