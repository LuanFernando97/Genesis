# Scheduler

## Overview

The Scheduler is responsible for managing future events inside the simulation.

It allows actions to be scheduled to execute at a specific simulation tick.

---

# Event Structure

Each event contains:

```
Event

 ├── tick
 ├── callback
 ├── args
 └── kwargs
```

Example:

```
Tick 100

Create a new individual
```

---

# Scheduling

Events are registered using:

```python
Scheduler.schedule()
```

The Scheduler stores future events and keeps them ordered by execution time.

Flow:

```
Scheduler.schedule()

        |
        v

Future Events List
```

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

Pending events are executed
```

---

# Example

Scheduled events:

```
Tick 50
  Create plant

Tick 100
  Create individual

Tick 200
  Change weather
```

When the Clock reaches the required tick:

```
Event executed
```

---

# Event Removal

After execution:

```
Event

   |
   v

Executed

   |
   v

Removed from Scheduler
```

Events are executed only once.

---

# Responsibility

The Scheduler does not know about the simulation world.

Its only responsibilities are:

- Knowing when an event should happen;
- Executing the associated callback.

The event itself contains the required behavior.