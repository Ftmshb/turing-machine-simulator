from simulator.constants import LEFT, RIGHT


class Rule:
    """
    Represents a single rule in a Universal Turing Machine description.

    A rule has the form:
                        (current_state,
                         read_symbol,
                         next_state,
                         write_symbol,
                         direction)
    """

    def __init__(
        self,
        current_state: str,
        read_symbol: str,
        next_state: str,
        write_symbol: str,
        direction: str,
    ):

        if not current_state:
            raise ValueError("Current state cannot be empty.")

        if not next_state:
            raise ValueError("Next state cannot be empty.")

        if len(read_symbol) != 1:
            raise ValueError("Read symbol must be a single character.")

        if len(write_symbol) != 1:
            raise ValueError("Write symbol must be a single character.")

        if direction not in (LEFT, RIGHT):
            raise ValueError("Direction must be LEFT or RIGHT.")

        self.current_state = current_state
        self.read_symbol = read_symbol
        self.next_state = next_state
        self.write_symbol = write_symbol
        self.direction = direction

    def __repr__(self) -> str:
        return (
            f"({self.current_state}, "
            f"{self.read_symbol}) -> "
            f"({self.next_state}, "
            f"{self.write_symbol}, "
            f"{self.direction})"
        )
