from __future__ import annotations

from collections import defaultdict
from uuid import uuid4


class EntityIdGenerator:
    def __init__(self) -> None:
        self._counters: dict[type, int] = defaultdict(int)

    def generate(self, entity_type: type) -> tuple[str, int]:
        self._counters[entity_type] += 1

        return str(uuid4()), self._counters[entity_type]
