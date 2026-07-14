import pytest

from simulator.state import State


def test_normal_state():
    state = State("q0")

    assert state.name == "q0"
    assert not state.is_accept
    assert not state.is_reject


def test_accept_state():
    state = State("q_accept", is_accept=True)

    assert state.is_accept
    assert not state.is_reject


def test_reject_state():
    state = State("q_reject", is_reject=True)

    assert state.is_reject
    assert not state.is_accept


def test_empty_name():
    with pytest.raises(ValueError):
        State("")


def test_accept_and_reject():
    with pytest.raises(ValueError):
        State(
            "q",
            is_accept=True,
            is_reject=True,
        )


def test_repr():
    state = State("q5")

    assert repr(state) == "q5"
