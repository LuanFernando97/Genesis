from genesis.core.clock import Clock


def test_clock_initial_state():
    clock = Clock()

    assert clock.current_tick == 0


def test_clock_tick_increases_tick():
    clock = Clock()

    clock.tick()

    assert clock.current_tick == 1


def test_clock_multiple_ticks():
    clock = Clock()

    clock.tick()
    clock.tick()
    clock.tick()

    assert clock.current_tick == 3


def test_clock_reset():
    clock = Clock()

    clock.tick()
    clock.tick()

    clock.reset()

    assert clock.current_tick == 0


def test_clock_manual_advance():
    clock = Clock()

    clock.advance(10)

    assert clock.current_tick == 10


def test_clock_tick_after_manual_advance():
    clock = Clock()

    clock.advance(10)
    clock.tick()

    assert clock.current_tick == 11


def test_clock_repr():
    clock = Clock()

    representation = repr(clock)

    assert representation == "<Clock current_tick=0>"
