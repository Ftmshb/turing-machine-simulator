from simulator.constants import BLANK_SYMBOL


class Tape:
    """
    Represents an infinite tape for a Turing Machine.

    The tape is implemented using a dictionary, allowing
    infinite expansion in both directions.
    """

    def __init__(self, input_string: str = ""):
        self.cells = {}

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

    def get_used_positions(self):
        """
        Return all positions that have been written to.
        """
        return sorted(self.cells.keys())
