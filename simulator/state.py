class State:
    """
    Represents a state in a Turing Machine.
    """

    def __init__(
        self,
        name: str,
        is_accept: bool = False,
        is_reject: bool = False,
    ):
        """
        Initialize a state.

        Args:
            name: Name of the state.
            is_accept: True if this is an accept state.
            is_reject: True if this is a reject state.
        """
        self.name = name
        self.is_accept = is_accept
        self.is_reject = is_reject