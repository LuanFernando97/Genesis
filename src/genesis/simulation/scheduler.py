from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Event:
    tick: int
    callback: Callable[..., Any]
    name: str = "Unnamed Event"
    args: tuple[Any, ...] = ()
    kwargs: dict[str, Any] = field(default_factory=dict)


class Scheduler:
    def __init__(self):
        self._events: list[Event] = []

    @property
    def events(self):
        return self._events

    def schedule(self, event: Event):
        self._events.append(event)
        self._events.sort(key=lambda e: e.tick)

    def remove(self, event: Event):
        self._events.remove(event)

    def pending_events(self, current_tick: int) -> list[Event]:
        return [event for event in self._events if event.tick <= current_tick]

    def execute(self, current_tick: int):
        events = self.pending_events(current_tick)

        for event in events:
            kwargs = event.kwargs or {}
            event.callback(*event.args, **kwargs)
            self.remove(event)
