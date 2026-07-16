from simulator.parser import Parser
from simulator.state import State

JSON_PATH = "machines/copy_machine.json"


def test_load_json():
    parser = Parser(JSON_PATH)

    assert isinstance(parser.data, dict)


def test_parse_states():
    parser = Parser(JSON_PATH)

    parser.parse_states()

    assert len(parser.states) == len(parser.data["states"])


def test_accept_state():
    parser = Parser(JSON_PATH)

    parser.parse_states()

    assert parser.states["qAccept"].is_accept


def test_reject_state():
    parser = Parser(JSON_PATH)

    parser.parse_states()

    assert parser.states["qReject"].is_reject


def test_parse_transitions():
    parser = Parser(JSON_PATH)

    parser.parse_transitions()

    assert len(parser.transitions) == len(parser.data["transitions"])


def test_transition_exists():
    parser = Parser(JSON_PATH)

    parser.parse_transitions()

    transition = parser.transitions[("qStart", "0")]

    assert transition.next_state == "qHave0"
    assert transition.write_symbol == "A"
    assert transition.direction == "R"


def test_parse_machine():
    parser = Parser(JSON_PATH)

    states, transitions, start_state = parser.parse_machine()

    assert isinstance(states, dict)
    assert isinstance(transitions, dict)
    assert isinstance(start_state, State)


def test_start_state():
    parser = Parser(JSON_PATH)

    _, _, start_state = parser.parse_machine()

    assert start_state.name == "qStart"