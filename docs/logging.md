# Logging Strategy

## Overview

Genesis uses Python's built-in `logging` module to monitor simulation execution.

The logging system was designed to support long-running simulations where different subsystems require independent monitoring.

---

# Logging Architecture

Each simulation execution creates a unique logging session.

Example:

```
logs/
└── 2026-07-10_14-30-00/
    ├── genesis.simulation.log
    ├── genesis.world.log
    ├── genesis.agent.log
    └── genesis.events.log
```

The directory represents a single simulation execution.

---

# Logger Creation

Loggers are retrieved through:

```python
get_logger(name)
```

Example:

```python
simulation_logger = get_logger("genesis.simulation")
world_logger = get_logger("genesis.world")
agent_logger = get_logger("genesis.agent")
```

The logger is created automatically if it does not exist.

If the logger already exists, the existing instance is returned.

---

# Log Levels

## DEBUG

Detailed information useful during development.

Example:

```
Agent evaluated possible actions
```

---

## INFO

Normal execution events.

Example:

```
Simulation started
```

---

## WARNING

Unexpected situations that do not stop execution.

Example:

```
Resource level below expected threshold
```

---

## ERROR

Execution errors.

Example:

```
Failed to save simulation state
```

---

## CRITICAL

Severe failures that may prevent execution.

Example:

```
Simulation cannot continue
```

---

# Rules

- Logs are used for monitoring and debugging.
- Logs do not replace simulation data.
- Each subsystem should use its own logger context.
- Generated logs are ignored by Git.
- Excessive DEBUG logging should be avoided in large simulations.

---

# Future Improvements

Possible future improvements:

- Log rotation
- Structured logs (JSON)
- Performance monitoring
- Simulation execution analysis