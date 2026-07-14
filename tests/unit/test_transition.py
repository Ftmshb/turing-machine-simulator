import pytest

from simulator.transition import Transition


def test_create_transition():
    """
    A transition should store all information correctly.
    """

    transition = Transition(
        current_state="q0",
        current_symbol="0",
        next_state="q1",
        write_symbol="X",
        direction="R",
    )

    assert transition.current_state == "q0"
    assert transition.current_symbol == "0"
    assert transition.next_state == "q1"
    assert transition.write_symbol == "X"
    assert transition.direction == "R"


def test_left_direction():
    """
    Transition should accept left movement.
    """

    transition = Transition(
        "q1",
        "1",
        "q2",
        "0",
        "L",
    )

    assert transition.direction == "L"


def test_right_direction():
    """
    Transition should accept right movement.
    """

    transition = Transition(
        "q2",
        "_",
        "q3",
        "_",
        "R",
    )

    assert transition.direction == "R"


def test_invalid_direction():
    """
    Invalid direction should raise an error.
    """

    with pytest.raises(ValueError):
        Transition(
            "q0",
            "0",
            "q1",
            "X",
            "S",
        )


def test_transition_with_accept_state():
    """
    Transition should allow moving to an accept state.
    """

    transition = Transition(
        "q5",
        "1",
        "qaccept",
        "1",
        "R",
    )

    assert transition.next_state == "qaccept"


def test_transition_with_reject_state():
    """
    Transition should allow moving to a reject state.
    """

    transition = Transition(
        "q5",
        "0",
        "qreject",
        "0",
        "L",
    )

    assert transition.next_state == "qreject"


def test_transition_values_are_independent():
    """
    Different transitions should store their own values.
    """

    transition1 = Transition(
        "q0",
        "0",
        "q1",
        "X",
        "R",
    )

    transition2 = Transition(
        "q2",
        "1",
        "q3",
        "Y",
        "L",
    )

    assert transition1.current_state != transition2.current_state
    assert transition1.write_symbol != transition2.write_symbol