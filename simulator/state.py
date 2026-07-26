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

        if not name:
            raise ValueError("State name cannot be empty.")

        if is_accept and is_reject:
            raise ValueError("State cannot be both accept and reject.")

        self.name = name
        self.is_accept = is_accept
        self.is_reject = is_reject

    def __repr__(self) -> str:
        return self.name
