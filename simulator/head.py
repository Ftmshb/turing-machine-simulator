from simulator.constants import LEFT, RIGHT


class Head:
    """
    Represents the read/write head of a Turing Machine.

    The head keeps track of its current position on the tape
    and can move left or right.
    """

    def __init__(self):
        """
        Initialize the head at the starting position (0).
        """
        self.position = 0

    def move(self, direction: str):

        if direction == LEFT:
            self.move_left()

        elif direction == RIGHT:
            self.move_right()

        else:
            raise ValueError("Invalid direction.")

    def move_left(self) -> None:
        """
        Move the head one cell to the left.
        """
        self.position -= 1

    def move_right(self) -> None:
        """
        Move the head one cell to the right.
        """
        self.position += 1

    def reset(self) -> None:
        """
        Reset the head to the starting position.
        """
        self.position = 0
