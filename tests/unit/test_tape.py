from simulator.tape import Tape
from simulator.constants import BLANK_SYMBOL


def test_initialize_with_input():
    """
    Tape should correctly store the initial input string.
    """
    tape = Tape("101")

    assert tape.read(0) == "1"
    assert tape.read(1) == "0"
    assert tape.read(2) == "1"


def test_initialize_without_input():
    """
    An empty tape should contain one blank symbol at position 0.
    """
    tape = Tape()

    assert tape.read(0) == BLANK_SYMBOL


def test_read_unwritten_position_returns_blank():
    """
    Reading an unwritten position should always return the blank symbol.
    """
    tape = Tape("101")

    assert tape.read(10) == BLANK_SYMBOL
    assert tape.read(-5) == BLANK_SYMBOL


def test_write_new_position():
    """
    Writing to a new position should store the symbol.
    """
    tape = Tape()

    tape.write(5, "X")

    assert tape.read(5) == "X"


def test_write_negative_position():
    """
    The tape must support negative positions.
    """
    tape = Tape()

    tape.write(-3, "Y")

    assert tape.read(-3) == "Y"


def test_overwrite_existing_position():
    """
    Writing to an existing position should overwrite the previous symbol.
    """
    tape = Tape("101")

    tape.write(1, "X")

    assert tape.read(1) == "X"


def test_get_used_positions():
    """
    Used positions should be returned in sorted order.
    """
    tape = Tape("10")

    tape.write(5, "X")
    tape.write(-2, "Y")

    assert tape.get_used_positions() == [-2, 0, 1, 5]
