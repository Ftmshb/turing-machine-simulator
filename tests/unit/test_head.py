import pytest

from simulator.head import Head
from simulator.constants import LEFT, RIGHT


def test_head_initial_position():
    head = Head()
    assert head.position == 0


def test_move_right():
    head = Head()
    head.move(RIGHT)
    assert head.position == 1


def test_move_left():
    head = Head()
    head.move(LEFT)
    assert head.position == -1


def test_multiple_moves():
    head = Head()

    head.move(RIGHT)
    head.move(RIGHT)
    head.move(LEFT)

    assert head.position == 1


def test_reset():
    head = Head()

    head.move(RIGHT)
    head.move(RIGHT)

    head.reset()

    assert head.position == 0


def test_invalid_direction():
    head = Head()

    with pytest.raises(ValueError):
        head.move("UP")
