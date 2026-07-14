from simulator.tape import Tape
from simulator.constants import BLANK_SYMBOL


def test_empty_tape():
    tape = Tape()

    assert tape.read(0) == BLANK_SYMBOL


def test_initial_input():
    tape = Tape("101")

    assert tape.read(0) == "1"
    assert tape.read(1) == "0"
    assert tape.read(2) == "1"


def test_blank_read():
    tape = Tape("1")

    assert tape.read(20) == BLANK_SYMBOL
    assert tape.read(-5) == BLANK_SYMBOL


def test_write():
    tape = Tape()

    tape.write(10, "A")

    assert tape.read(10) == "A"


def test_write_negative():
    tape = Tape()

    tape.write(-3, "X")

    assert tape.read(-3) == "X"


def test_used_positions():
    tape = Tape()

    tape.write(4, "A")
    tape.write(-2, "B")

    assert tape.get_used_positions() == [-2, 0, 4]


def test_min_max():
    tape = Tape()

    tape.write(5, "A")
    tape.write(-7, "B")

    assert tape.get_min_position() == -7
    assert tape.get_max_position() == 5


def test_render():
    tape = Tape("10")

    text, start = tape.render(0)

    assert isinstance(text, str)
    assert isinstance(start, int)