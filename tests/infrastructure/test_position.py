from genesis.infrastructure.position import Position


def test_create_position():
    position = Position(10, 5)

    assert position.x == 10
    assert position.y == 5


def test_compare_positions():
    position_a = Position(10, 5)
    position_b = Position(10, 5)
    position_c = Position(5, 10)

    assert position_a == position_b
    assert position_a != position_c


def test_add_positions():
    position_a = Position(10, 5)
    position_b = Position(2, 3)

    result = position_a + position_b

    assert result == Position(12, 8)


def test_subtract_positions():
    position_a = Position(10, 5)
    position_b = Position(2, 3)

    result = position_a - position_b

    assert result == Position(8, 2)


def test_position_repr():
    position = Position(10, 5)

    assert repr(position) == "Position(x=10, y=5)"
