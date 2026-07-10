# Clock

## Overview

The Clock is responsible for managing the internal time of the simulation.

It is independent from real-world time.

---

# Concept

The simulation uses ticks as its internal time unit.

Example:

```
Real time:
5 seconds

Simulation speed:
10x

Simulation time:
50 ticks
```

---

# Responsibilities

The Clock is responsible for:

- Storing the current simulation time;
- Advancing simulation time;
- Providing the current tick value;
- Resetting simulation time.

---

# Tick Flow

During each simulation tick:

```
Simulation.tick()

        |
        v

Clock.tick()

        |
        v

current_tick += 1
```

---

# Example

Initial state:

```
current_tick = 0
```

After:

```python
clock.tick()
```

The result is:

```
current_tick = 1
```

---

# Real Time vs Simulation Time

The engine has two different time concepts.

## Real Time

The actual time passing on the computer.

Example:

```
1 second
```

---

## Simulation Time

The internal time controlled by the Clock.

Example:

```
1 tick
```

The simulation speed defines the relationship between these two values.