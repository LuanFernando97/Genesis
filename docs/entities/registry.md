# Entity Registry

## Overview

The `EntityRegistry` is responsible for storing and managing active entities inside the Genesis simulation.

It provides a centralized mechanism for tracking entities during their lifecycle.

The registry does not create or destroy entities. It only manages the collection of active entities.

---

# Responsibilities

The `EntityRegistry` is responsible for:

- Registering created entities.
- Removing destroyed entities.
- Retrieving entities by UUID.
- Iterating over active entities.
- Tracking the number of registered entities.

---

# Architecture

The registry stores entities using their UUID as the key.

```
EntityRegistry

{
    UUID: Entity
}
```

Example:

```
{
    "550e8400-e29b-41d4-a716-446655440000": Human_1,
    "8c7d5f2a-7e6b-4f2a": Animal_1
}
```

---

# Registration

Entities are automatically registered during the spawn process.

Example:

```python
human = Human.spawn(simulation)
```

After spawning:

```
EntityRegistry

Human_1
```

The registry now considers the entity active.

---

# Removal

Entities are removed from the registry during the despawn process.

Example:

```python
human.despawn()
```

Before:

```
EntityRegistry

Human_1
Animal_1
```

After:

```
EntityRegistry

Animal_1
```

Removed entities are no longer considered active simulation entities.

---

# Entity Lookup

Entities can be retrieved using their UUID.

Example:

```python
registry.get(entity.id)
```

Returns:

- The registered entity when found.
- `None` when the entity does not exist.

---

# Iteration

The registry allows iteration over all active entities.

Example:

```python
for entity in registry:
    print(entity)
```

Only currently active entities are returned.

Destroyed entities are not included.

---

# Entity Count

The number of active entities can be obtained through the registry size.

Example:

```python
len(registry)
```

Returns the amount of currently registered entities.

---

# Design Decisions

## Registry Uses UUID as Key

The registry uses UUIDs instead of display IDs.

Reasons:

- UUIDs are globally unique.
- Display IDs are only for visualization.
- Different entity types may share the same display ID.

Example:

```
Human_1
Animal_1
```

Both are valid because their UUIDs are different.

---

## Registry Encapsulation

The registry is an internal component of the entity system.

External systems should interact with entities through controlled interfaces instead of directly modifying registry data.

This keeps entity state consistent and reduces coupling.

---

# Future Extensions

Possible future improvements:

- Entity queries.
- Filtering by entity type.
- Spatial indexing.
- Population management.
- Persistence support.
- Historical entity tracking.