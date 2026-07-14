from simulator.state import State


def test_create_normal_state():
    state = State("q0")

    assert state.name == "q0"
    assert state.is_accept is False
    assert state.is_reject is False


def test_create_accept_state():
    state = State("accept", is_accept=True)

    assert state.name == "accept"
    assert state.is_accept is True
    assert state.is_reject is False


def test_create_reject_state():
    state = State("reject", is_reject=True)

    assert state.name == "reject"
    assert state.is_accept is False
    assert state.is_reject is True