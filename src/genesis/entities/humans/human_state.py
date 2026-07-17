from enum import StrEnum


class HumanState(StrEnum):
    IDLE = "idle"

    # Movement
    WALKING = "walking"
    RUNNING = "running"

    # Survival
    SLEEPING = "sleeping"
    EATING = "eating"
    DRINKING = "drinking"

    # Resource gathering
    GATHERING = "gathering"
    HARVESTING = "harvesting"
    MINING = "mining"
    CHOPPING = "chopping"

    # Construction
    BUILDING = "building"
    REPAIRING = "repairing"

    # Work
    CRAFTING = "crafting"

    # Social
    TALKING = "talking"

    # Combat
    ATTACKING = "attacking"
    FLEEING = "fleeing"

    # Life cycle
    DEAD = "dead"
