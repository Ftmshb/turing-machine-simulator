from simulator.constants import LEFT, RIGHT

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

        if direction not in (LEFT, RIGHT):
            raise ValueError("Direction must be LEFT or RIGHT.")

        self.current_state = current_state
        self.current_symbol = current_symbol
        self.next_state = next_state
        self.write_symbol = write_symbol
        self.direction = direction

    def __repr__(self) -> str:
        return (
            f"{self.current_state} "
            f"--{self.current_symbol}/"
            f"{self.write_symbol},"
            f"{self.direction}--> "
            f"{self.next_state}"
        )