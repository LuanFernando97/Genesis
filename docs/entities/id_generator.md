# Entity ID Generator

## Overview

The `EntityIdGenerator` is responsible for creating identifiers for entities inside the Genesis simulation.

Each entity receives two identifiers:

- A UUID for internal identification.
- A sequential display ID for human-readable representation.

The generator separates internal identity from visual representation.

---

# Responsibilities

The `EntityIdGenerator` is responsible for:

- Generating unique entity UUIDs.
- Creating incremental display IDs.
- Maintaining display ID sequences per entity type.
- Preventing display ID reuse during execution.

---

# UUID Generation

Each entity receives a UUID as its primary identifier.

The UUID is:

- Globally unique.
- Used internally by the simulation.
- Used for entity lookup and references.
- Independent from display identifiers.

Example:

```
550e8400-e29b-41d4-a716-446655440000
```

---

# Display ID Generation

The generator creates a sequential identifier for each entity type.

Examples:

```
Human_1
Human_2
Human_3

Animal_1
Animal_2
```

Each entity type maintains its own counter.

Example:

```python
human_1 = Human.spawn(simulation)
human_2 = Human.spawn(simulation)
animal_1 = Animal.spawn(simulation)
```

Generated display IDs:

```
Human_1
Human_2
Animal_1
```

---

# ID Lifetime

Display IDs are not reused during execution.

Example:

Initial entities:

```
Human_1
Human_2
```

After:

```
Human_2.despawn()
```

A new entity receives:

```
Human_3
```

The counter always increases.

---

# Design Decisions

## UUID and Display ID Separation

UUID and display ID have different purposes.

## UUID

Used for:

- Internal identity.
- Entity references.
- Registry lookup.

Properties:

- Unique.
- Not human-readable.
- Suitable for persistence.

---

## Display ID

Used for:

- Logs.
- Debugging.
- Visualization.

Properties:

- Human-readable.
- Sequential.
- Easier to understand during development.

---

# Future Extensions

Possible future improvements:

- Persistent entity identifiers.
- Save/load compatibility.
- Distributed ID generation.
- Entity history tracking.