import json
from simulator.state import State
from simulator.transition import Transition


class Parser:
    """Parse a Turing Machine description from a JSON file."""

    def __init__(self, file_path: str):
        """Initialize the parser."""

        self.file_path = file_path
        self.data = self.load_json()

        self.states = {}
        self.transitions = {}
        self.start_state = None

    def load_json(self) -> dict:
        """Load a JSON file."""

        with open(self.file_path, "r", encoding="utf-8") as json_file:
            return json.load(json_file)

    def parse_states(self) -> None:
        """Create State objects."""

        accept_states = set(self.data["accept_states"])
        reject_states = set(self.data["reject_states"])

        for name in self.data["states"]:
            self.states[name] = State(
                name=name,
                is_accept=name in accept_states,
                is_reject=name in reject_states,
            )

    def parse_transitions(self) -> None:
        """Create Transition objects."""

        for transition_data in self.data["transitions"]:

            transition = Transition(
                current_state=transition_data["current_state"],
                current_symbol=transition_data["read"],
                next_state=transition_data["next_state"],
                write_symbol=transition_data["write"],
                direction=transition_data["move"],
            )

            key = (
                transition.current_state,
                transition.current_symbol,
            )

            self.transitions[key] = transition

    def parse_machine(
        self,
    ) -> tuple[
        dict[str, State],
        dict[tuple[str, str], Transition],
        State,
    ]:
        """Parse the complete Turing Machine."""

        self.parse_states()
        self.parse_transitions()

        self.start_state = self.states[self.data["start_state"]]

        return (
            self.states,
            self.transitions,
            self.start_state,
        )
