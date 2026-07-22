# Item

## Overview

`Item` is the abstract base class for every item that can exist in the simulation.

It defines the common information shared by all items while allowing specialized item types to extend its behavior.

An `Item` cannot be instantiated directly.

---

# Responsibilities

The `Item` class is responsible for:

- Representing a generic item.
- Storing its name.
- Storing its description.
- Providing a common interface for all item types.

---

# Construction

Because the class is abstract, it must be inherited.

Example:

```python
class Apple(Item):

    def __init__(self):
        super().__init__(
            name="Apple",
            description="A fresh apple."
        )
```

---

# Attributes

Every item contains the following information.

| Attribute | Description |
|-----------|-------------|
| Name | Item name |
| Description | Optional description |

Both attributes are exposed through read-only properties.

---

# Validation

The constructor validates the provided information.

| Validation | Behavior |
|------------|----------|
| Empty name | Raises `ValueError` |

Descriptions are optional.

---

# Design

`Item` intentionally contains very little behavior.

Future subclasses will extend it with additional information such as:

- Weight
- Value
- Durability
- Stack size
- Equipment slots
- Consumable effects
- Crafting recipes

The current implementation serves as the common foundation for every item in Genesis.