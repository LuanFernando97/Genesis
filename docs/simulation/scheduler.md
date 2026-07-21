# Scheduler

## Overview

The Scheduler is responsible for managing future events inside the simulation.

It allows actions to be scheduled to execute at a specific simulation tick.

The Scheduler is completely generic and does not know anything about the world, entities or game logic. Its only responsibility is executing callbacks when their scheduled tick is reached.

---

# Event Structure

Each event contains:

```
Event

 ├── tick
 ├── callback
 ├── name
 ├── args
 └── kwargs
```

| Field | Description |
|-------|-------------|
| tick | Simulation tick when the event should execute. |
| callback | Function or method to execute. |
| name | Human-readable event name for debugging and logging. |
| args | Positional arguments passed to the callback. |
| kwargs | Keyword arguments passed to the callback. |

Example:

```
Tick 100

Spawn Human
```

---

# Scheduling

Events are registered using:

```python
Scheduler.schedule()
```

The Scheduler stores future events ordered by their execution tick.

Flow:

```
Scheduler.schedule()

        |
        v

Future Events List
```

Events scheduled for earlier ticks are always executed first.

---

# Execution

During each simulation tick:

```
Simulation.tick()

        |
        v

Scheduler.execute()

        |
        v
Execute pending events
```

Every event whose scheduled tick is less than or equal to the current simulation tick is executed.

After execution, the event is automatically removed from the scheduler.

---

# Recurring Events

The Scheduler also supports recurring systems.

A callback may schedule a new event for itself during execution.

Example:

```
Tick 1

Update Entities

        │
        v

Schedules

        │
        v

Update Entities

Tick 2
```

This mechanism is used by the simulation to continuously update all registered entities without scheduling one event per entity.

---

# Example

Scheduled events:

```
Tick 50
    Spawn Tree

Tick 100
    Spawn Human

Tick 200
    Change Weather
```

When the simulation reaches the corresponding tick, each callback is executed.

---

# Event Removal

The lifecycle of an event is:

```
Scheduled

    │
    v

Executed

    │
    v

Removed
```

Events execute only once unless the callback schedules a new event.

---

# Responsibilities

The Scheduler has a single responsibility:

- Store future events.
- Execute events at the correct simulation tick.

The Scheduler does **not**:

- Update the world.
- Manage entities.
- Control simulation time.
- Implement game logic.

Those responsibilities belong to other simulation systems.

---

# Design Principles

The Scheduler follows an event-driven architecture.

```
Simulation

    │
    v

Scheduler

    │
    v

Event

    │
    v

Callback
```

This design keeps the Scheduler completely independent from the rest of the simulation while allowing any system to schedule future actions.