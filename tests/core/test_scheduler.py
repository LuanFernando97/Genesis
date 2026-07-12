from genesis.simulation.scheduler import Event, Scheduler


def test_schedule_event():
    scheduler = Scheduler()

    event = Event(
        tick=10,
        callback=lambda: None,
    )

    scheduler.schedule(event)

    assert len(scheduler.events) == 1


def test_events_are_sorted():
    scheduler = Scheduler()

    scheduler.schedule(Event(10, lambda: None))
    scheduler.schedule(Event(5, lambda: None))
    scheduler.schedule(Event(20, lambda: None))

    assert scheduler.events[0].tick == 5


def test_pending_events():
    scheduler = Scheduler()

    scheduler.schedule(Event(5, lambda: None))
    scheduler.schedule(Event(10, lambda: None))

    pending = scheduler.pending_events(5)

    assert len(pending) == 1
    assert pending[0].tick == 5


def test_execute_event():
    scheduler = Scheduler()

    executed = False

    def callback():
        nonlocal executed
        executed = True

    scheduler.schedule(Event(5, callback))

    scheduler.execute(5)

    assert executed


def test_event_removed_after_execution():
    scheduler = Scheduler()

    scheduler.schedule(Event(5, lambda: None))

    scheduler.execute(5)

    assert len(scheduler.events) == 0


def test_future_event_is_not_executed():
    scheduler = Scheduler()

    executed = False

    def callback():
        nonlocal executed
        executed = True

    scheduler.schedule(Event(10, callback))

    scheduler.execute(5)

    assert not executed


def test_event_arguments():
    scheduler = Scheduler()

    result = []

    def callback(value):
        result.append(value)

    scheduler.schedule(
        Event(
            tick=5,
            callback=callback,
            args=("Genesis",),
        )
    )

    scheduler.execute(5)

    assert result == ["Genesis"]


def test_multiple_events_same_tick():
    scheduler = Scheduler()

    executed = []

    scheduler.schedule(Event(5, lambda: executed.append(1)))

    scheduler.schedule(Event(5, lambda: executed.append(2)))

    scheduler.execute(5)

    assert executed == [1, 2]
