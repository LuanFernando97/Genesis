from genesis.entities.humans.human_state import HumanState


def test_human_state_has_idle():
    assert HumanState.IDLE == "idle"


def test_human_state_has_walking():
    assert HumanState.WALKING == "walking"


def test_human_state_has_sleeping():
    assert HumanState.SLEEPING == "sleeping"
