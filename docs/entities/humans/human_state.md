# HumanState

## Overview

`HumanState` is an enumeration that represents the current activity performed by a human.

The state provides a simple way to describe what a human is currently doing and serves as the foundation for future behavior and AI systems.

---

# Purpose

The current state allows the simulation to determine how a human should behave during each update.

Example:

```
Human
    │
    ▼
Current State
    │
    ├── IDLE
    ├── WALKING
    ├── EATING
    ├── SLEEPING
    └── ...
```

Different states may consume or restore needs at different rates.

---

# Available States

| State | Description |
|--------|-------------|
| IDLE | Human is doing nothing. |
| WALKING | Human is moving. |
| RUNNING | Human is moving quickly. |
| SLEEPING | Human is sleeping. |
| EATING | Human is eating. |
| DRINKING | Human is drinking. |
| GATHERING | Human is collecting resources. |
| HARVESTING | Human is harvesting crops. |
| MINING | Human is mining resources. |
| CHOPPING | Human is cutting trees. |
| BUILDING | Human is constructing structures. |
| REPAIRING | Human is repairing structures. |
| CRAFTING | Human is producing items. |
| TALKING | Human is interacting with another human. |
| ATTACKING | Human is engaged in combat. |
| FLEEING | Human is escaping danger. |
| DEAD | Human is dead. |

---

# Default State

Every human starts in the `IDLE` state.

```python
human = Human(...)

assert human.state == HumanState.IDLE
```

---

# Changing State

The current state can be modified during the simulation.

```python
human.state = HumanState.WALKING
```

Only values of type `HumanState` are accepted.

Assigning any other type raises a `TypeError`.

---

# Integration

`HumanState` belongs to the `Human` class.

```
Human
    │
    └── HumanState
```

During each simulation tick, the current state influences the human's behavior.

At the current stage of the project, the state system is intentionally simple and serves as the basis for future AI.

---

# Future Improvements

Future versions may replace or extend `HumanState` with a more advanced behavior system.

Possible additions include:

- Decision making
- Task execution
- Behavior trees
- Goal-oriented AI
- Utility AI
- State transitions
- Action planning

The current enumeration provides a lightweight foundation while keeping the architecture simple during the early stages of development.