import pytest

from simulator.transition import Transition
from simulator.constants import LEFT, RIGHT


def test_transition_creation():
    t = Transition(
        "q0",
        "0",
        "q1",
        "1",
        RIGHT,
    )

    assert t.current_state == "q0"
    assert t.next_state == "q1"


def test_invalid_direction():
    with pytest.raises(ValueError):

        Transition(
            "q0",
            "0",
            "q1",
            "1",
            "UP",
        )


def test_repr():
    t = Transition(
        "q0",
        "0",
        "q1",
        "1",
        LEFT,
    )

    assert "q0" in repr(t)
    assert "q1" in repr(t)
