# Entity System

## Overview

The `Entity` class is the base abstraction for all objects that can exist inside the Genesis simulation.

Entities represent objects with identity and lifecycle. Concrete entity types will extend this base class in future phases.

Examples of future entities:

- Human
- Animal
- Plant
- Other autonomous agents

The current implementation provides the foundation required for entity creation, identification, registration, and lifecycle management.

---

# Responsibilities

The `Entity` class is responsible for:

- Storing the simulation reference.
- Generating entity identifiers.
- Managing entity lifecycle.
- Registering new entities.
- Removing destroyed entities.
- Providing common behavior for all entity types.

---

# Architecture

```
Entity
│
├── EntityIdGenerator
│
└── EntityRegistry
```

The entity system is independent from concrete entity implementations.

Future entity classes should inherit from `Entity` and extend its behavior.

Example:

```python
class Human(Entity):
    pass
```

---

# Identification

Every entity receives two identifiers.

## UUID

The UUID is the unique internal identifier of the entity.

Properties:

- Globally unique.
- Used internally for entity lookup.
- Never reused during execution.

Example:

```
550e8400-e29b-41d4-a716-446655440000
```

---

## Display ID

The display ID is an incremental identifier used for human-readable representation.

Examples:

```
Human_1
Human_2
Animal_1
Animal_2
```

The display ID exists only for visualization and debugging.

---
# Lifecycle

Entities have a simple lifecycle.

```
spawn()
   |
   v
Created
   |
   v
Alive
   |
   v
despawn()
   |
   v
Destroyed
```

---

# Spawn

Entities are created using the class method `spawn()`.

Example:

```python
human = Human.spawn(simulation)
```

The spawn process:

1. Creates the entity instance.
2. Generates entity identifiers.
3. Registers the entity.
4. Returns the created entity.

After spawning:

```python
human.is_alive == True
```

---

# Despawn

Entities can be removed from the simulation using `despawn()`.

Example:

```python
human.despawn()
```

The despawn process:

1. Removes the entity from the registry.
2. Marks the entity as destroyed.

After despawn:

```python
human.is_alive == False
```

Destroyed entities are no longer considered active simulation objects.

---

# Design Decisions

## Entity Owns Its Lifecycle

Entity lifecycle is managed by the entity itself.

The simulation does not know about specific entity types.

Preferred:

```python
Human.spawn(simulation)
```

Instead of:

```python
simulation.spawn(Human)
```

This keeps the simulation engine independent from future entity implementations.

---

# Future Extensions

Future phases may introduce:

- Entity attributes
- Behaviors
- Perception
- Decision making
- Reproduction
- Aging
- Death causes
- Entity interactions
  