from simulator.head import Head


def test_initial_position():
    """
    The head should start at position 0.
    """
    head = Head()

    assert head.position == 0


def test_move_right():
    """
    Moving right should increase the position by one.
    """
    head = Head()

    head.move_right()

    assert head.position == 1


def test_move_left():
    """
    Moving left should decrease the position by one.
    """
    head = Head()

    head.move_left()

    assert head.position == -1


def test_multiple_movements():
    """
    The head should correctly update its position after multiple moves.
    """
    head = Head()

    head.move_right()
    head.move_right()
    head.move_left()
    head.move_right()

    assert head.position == 2


def test_reset():
    """
    Reset should return the head to the initial position.
    """
    head = Head()

    head.move_right()
    head.move_right()
    head.move_left()

    head.reset()

    assert head.position == 0


def test_move_left_multiple_times():
    """
    The head should support moving to negative positions.
    """
    head = Head()

    head.move_left()
    head.move_left()
    head.move_left()

    assert head.position == -3


def test_move_right_multiple_times():
    """
    The head should support moving to large positive positions.
    """
    head = Head()

    for _ in range(10):
        head.move_right()

    assert head.position == 10