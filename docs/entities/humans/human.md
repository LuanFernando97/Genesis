# Human

## Overview

The `Human` class represents the first autonomous agent implemented in Genesis.

A `Human` is an `Entity` capable of existing inside the simulation, maintaining its own internal state, needs, inventory and position in the world.

At every simulation tick, each human updates itself through the `update()` method, allowing future behaviors such as movement, decision making and interaction with the environment.

---

# Responsibilities

The `Human` class is responsible for:

- Representing an individual inside the simulation.
- Storing permanent identity information.
- Managing its basic needs.
- Maintaining its current position.
- Holding an inventory.
- Tracking its current state.
- Updating itself every simulation tick.

The class **does not** decide how the simulation works or how entities are scheduled. Those responsibilities belong to the `Simulation` and `Scheduler`.

---

# Class Diagram

```
Entity
   │
   └── Human
          ├── Needs
          ├── Inventory
          ├── Position
          ├── HumanState
          └── Sex
```

---

# Construction

A human is created by providing its permanent identity and initial state.

```python
human = Human(
    name="John",
    sex=Sex.MALE,
    age=25,
    position=Position(10, 5),
)
```

Optional components can also be provided.

```python
human = Human(
    name="John",
    sex=Sex.MALE,
    age=25,
    position=Position(10, 5),
    needs=Needs(),
    inventory=Inventory(),
    state=HumanState.IDLE,
)
```

---

# Identity

Each human possesses immutable identity information.

| Attribute | Description |
|-----------|-------------|
| Name | Human name |
| Sex | Biological sex |
| Age | Current age |

Identity values are validated during construction.

---

# Needs

Every human owns a `Needs` object responsible for storing its physical condition.

Current needs include:

- Energy
- Hunger
- Thirst
- Health

Needs are updated every simulation tick.

---

# Position

Humans always possess a valid world position.

```python
human.position
```

The position can be modified during the simulation.

```python
human.position = Position(15, 20)
```

---

# Inventory

Every human owns exactly one inventory.

If no inventory is provided during construction, an empty inventory is created automatically.

```python
human.inventory
```

---

# State

The current activity of a human is represented by `HumanState`.

Initially every human starts as:

```python
HumanState.IDLE
```

The state system will be expanded in future phases to support more complex behaviors.

---

# Update Cycle

The simulation calls `update()` once per simulation tick.

Current implementation:

```
Simulation Tick
        │
        v
Human.update()
        │
        ├── Update Needs
        └── Update State
```

At the moment the update performs:

- Decrease energy.
- Increase hunger.
- Increase thirst.
- Update internal state.

Future phases will extend this method with:

- Decision making
- Movement
- Interactions
- Jobs
- AI
- Relationships

---

# Integration with Simulation

Humans are updated automatically by the simulation.

The `Simulation` schedules an entity update event every tick, which iterates through all registered entities and invokes:

```python
entity.update()
```

This design keeps the `Human` independent from the simulation loop.

---

# Validation Rules

The constructor validates all required information.

| Validation | Behavior |
|------------|----------|
| Empty name | Raises `ValueError` |
| Negative age | Raises `ValueError` |
| Invalid position | Raises `TypeError` |
| Invalid state | Raises `TypeError` |

---

# Design Principles

The class follows a composition-based design.

Instead of implementing every responsibility directly, it delegates functionality to specialized components.

```
Human
├── Needs
├── Inventory
├── Position
└── HumanState
```

This keeps the class cohesive and allows each component to evolve independently.

---

# Future Improvements

Planned features include:

- Aging
- Professions
- Skills
- Relationships
- Personality
- Goals
- Decision making
- Movement
- Pathfinding
- Equipment
- Combat
- Sleep cycle
- Eating
- Drinking
- AI behaviors

These features will be implemented incrementally in future phases without requiring major modifications to the current architecture.