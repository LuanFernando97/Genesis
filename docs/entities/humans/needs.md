# Needs

## Overview

The `Needs` class represents the physical condition of a human.

It encapsulates the basic physiological attributes that change over time during the simulation and provides a safe interface for modifying them while enforcing valid limits.

A `Needs` object is owned by exactly one `Human`.

---

# Responsibilities

The `Needs` class is responsible for:

- Storing physical needs.
- Validating initial values.
- Preventing invalid values.
- Providing methods to increase or decrease each need.
- Ensuring all values remain within valid limits.

---

# Attributes

The class currently manages four attributes.

| Attribute | Range | Description |
|----------|:-----:|-------------|
| Energy | 0–100 | Represents the available physical energy. |
| Hunger | 0–100 | Represents how hungry the human is. |
| Thirst | 0–100 | Represents how thirsty the human is. |
| Health | 0–100 | Represents the overall physical condition. |

All values are exposed through read-only properties.

---

# Construction

Needs can be created with default values.

```python
needs = Needs()
```

Or customized during construction.

```python
needs = Needs(
    energy=80,
    hunger=20,
    thirst=10,
    health=100,
)
```

---

# Validation

Every value must remain between **0** and **100**.

Attempting to create a `Needs` object with invalid values raises a `ValueError`.

```python
Needs(energy=-1)

Needs(hunger=120)
```

---

# Modifying Needs

Each attribute provides methods for increasing and decreasing its value.

Example:

```python
needs.increase_hunger(5)
needs.decrease_energy(2)
needs.increase_health(10)
```

Values are automatically clamped to the valid interval.

Example:

```
Energy = 98

increase_energy(10)

↓

Energy = 100
```

Likewise,

```
Energy = 2

decrease_energy(10)

↓

Energy = 0
```

---

# Integration

The `Needs` object is owned by a `Human`.

```
Human
    │
    └── Needs
            ├── Energy
            ├── Hunger
            ├── Thirst
            └── Health
```

The simulation updates these values automatically every tick through `Human.update()`.

---

# Future Improvements

Future versions may include additional needs such as:

- Sleep
- Happiness
- Stress
- Hygiene
- Body Temperature
- Morale
- Fatigue
- Comfort

The current implementation was designed to allow new needs to be added without changing the public interface.