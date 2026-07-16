from simulator.constants import BLANK_SYMBOL


class Tape:
    """
    Represents an infinite tape for a Turing Machine.

    The tape is implemented using a dictionary, allowing
    infinite expansion in both directions.
    """
    def __init__(self, input_string: str = ""):

        if not isinstance(input_string, str):
            raise TypeError("Input must be a string.")

        self.cells: dict[int, str] = {}

        if input_string:
            for index, symbol in enumerate(input_string):
                self.cells[index] = symbol
        else:
            self.cells[0] = BLANK_SYMBOL

    def read(self, position: int) -> str:
        """
        Read the symbol at the specified position.
        Returns the blank symbol if the position has not been written.
        """
        return self.cells.get(position, BLANK_SYMBOL)

    def write(self, position: int, symbol: str) -> None:
        """
        Write a symbol to the specified position.
        """
        self.cells[position] = symbol

    def get_used_positions(self) -> list[int]:
        """
        Return all positions that have been written to.
        """
        return sorted(self.cells.keys())

    def get_min_position(self) -> int:
        """
        Return the smallest used tape position.
        """
        return min(self.cells.keys())

    def get_max_position(self) -> int:
        """
        Return the largest used tape position.
        """
        return max(self.cells.keys())

    def render(self, head_position: int) -> tuple[str, int]:
        """
        Return the tape as a printable string and
        the first tape position displayed.
        """

        # Show negative positions only if they have actually been used
        start = min(0, self.get_min_position())

        # Show tape up to the furthest written cell or head position
        end = max(head_position, self.get_max_position())

        symbols = []

        for position in range(start, end + 1):
            symbols.append(self.read(position))

        return " ".join(symbols), start