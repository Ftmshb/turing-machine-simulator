class Transition:
    """
    Represents a transition in a Turing Machine.
    """

    def __init__(
        self,
        current_state: str,
        current_symbol: str,
        next_state: str,
        write_symbol: str,
        direction: str,
    ):
        """
        Initialize a transition.
        """

        if direction not in ("L", "R"):
            raise ValueError("Direction must be 'L' or 'R'.")

        self.current_state = current_state
        self.current_symbol = current_symbol
        self.next_state = next_state
        self.write_symbol = write_symbol
        self.direction = direction