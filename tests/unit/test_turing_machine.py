from simulator.head import Head
from simulator.state import State
from simulator.tape import Tape
from simulator.transition import Transition
from simulator.turing_machine import TuringMachine

from simulator.constants import RIGHT


def build_machine():

    states = {
        "q0": State("q0"),
        "qa": State("qa", is_accept=True),
        "qr": State("qr", is_reject=True),
    }

    transitions = {
        ("q0", "1"): Transition(
            "q0",
            "1",
            "qa",
            "1",
            RIGHT,
        )
    }

    tape = Tape("1")

    head = Head()

    return TuringMachine(
        states,
        transitions,
        states["q0"],
        tape,
        head,
    )


def test_current_symbol():

    tm = build_machine()

    assert tm.get_current_symbol() == "1"


def test_find_transition():

    tm = build_machine()

    assert tm.find_transition() is not None


def test_step():

    tm = build_machine()

    assert tm.step()

    assert tm.current_state.name == "qa"

    assert tm.head.position == 1

    assert tm.step_count == 1


def test_accept():

    tm = build_machine()

    tm.step()

    assert tm.is_accept()


def test_not_reject():

    tm = build_machine()

    assert not tm.is_reject()


def test_timeout():

    tm = build_machine()

    tm.max_steps = 1

    tm.step()

    assert tm.has_timed_out()


def test_no_transition():

    states = {
        "q0": State("q0"),
    }

    tape = Tape("0")

    tm = TuringMachine(
        states,
        {},
        states["q0"],
        tape,
        Head(),
    )

    assert tm.step() is False