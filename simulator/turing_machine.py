from simulator.constants import (
    ACCEPT,
    REJECT,
    TIMEOUT,
    DEFAULT_MAX_STEPS,
)

from simulator.tape import Tape
from simulator.head import Head
from simulator.state import State
from simulator.transition import Transition


class TuringMachine:
    """
    Represents a deterministic single-tape Turing Machine simulator.

    This class supports:
    States
    Input Alphabet
    Tape Alphabet
    Transition Function
    Start State
    qacc / qrej : Halting States
    """

    def __init__(
        self,
        states: dict[str, State],
        transitions: dict[tuple[str, str], Transition],
        start_state: State,
        tape: Tape,
        head: Head,
        input_alphabet: set[str],
        tape_alphabet: set[str],
        max_steps: int = DEFAULT_MAX_STEPS,
    ):
        """
        Initialize the Turing Machine.

        Args:
            states: Set of machine states.
            transitions: Transition function.
            start_state: Initial state.
            tape: Machine tape.
            head: Machine head.
            input_alphabet: Input alphabet.
            tape_alphabet: Tape alphabet.
            max_steps: Maximum execution steps.
        """

        # ---------------- Validation ----------------

        if max_steps <= 0:
            raise ValueError("max_steps must be greater than zero.")

        if not states:
            raise ValueError("States cannot be empty.")

        if start_state.name not in states:
            raise ValueError("Start state must exist in states.")

        if not input_alphabet:
            raise ValueError("Input alphabet cannot be empty.")

        if not tape_alphabet:
            raise ValueError("Tape alphabet cannot be empty.")

        # The input alphabet must be a subset of the tape alphabet
        if not input_alphabet.issubset(tape_alphabet):
            raise ValueError("Input alphabet must be a subset of tape alphabet.")

        # Validate transitions
        for transition in transitions.values():

            if transition.current_state not in states:
                raise ValueError(
                    f"Undefined current state: " f"{transition.current_state}"
                )

            if transition.next_state not in states:
                raise ValueError(f"Undefined next state: " f"{transition.next_state}")

            if transition.current_symbol not in tape_alphabet:
                raise ValueError(
                    f"Invalid read symbol: " f"{transition.current_symbol}"
                )

            if transition.write_symbol not in tape_alphabet:
                raise ValueError(f"Invalid write symbol: " f"{transition.write_symbol}")

        # ---------------- Store machine ----------------

        self.states = states
        self.transitions = transitions

        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet

        self.current_state = start_state

        self.tape = tape
        self.head = head

        self.max_steps = max_steps
        self.step_count = 0

    def validate_input(self, input_string: str) -> None:
        """
        Validate input string according to Σ.
        """

        for symbol in input_string:

            if symbol not in self.input_alphabet:
                raise ValueError(f"Invalid input symbol: {symbol}")

    def get_current_symbol(self) -> str:
        """
        Return symbol under the head.
        """

        return self.tape.read(self.head.position)

    def find_transition(self) -> Transition | None:
        """
        Find transition based on current state and symbol.
        """

        key = (
            self.current_state.name,
            self.get_current_symbol(),
        )

        return self.transitions.get(key)

    def step(self) -> bool:
        """
        Execute one transition.
        """

        transition = self.find_transition()

        if transition is None:
            return False

        # Validate written symbol
        if transition.write_symbol not in self.tape_alphabet:
            raise ValueError(f"Invalid tape symbol: " f"{transition.write_symbol}")

        # Write symbol
        self.tape.write(
            self.head.position,
            transition.write_symbol,
        )

        # Move head
        self.head.move(transition.direction)

        # Change state
        self.current_state = self.states[transition.next_state]

        self.step_count += 1

        return True

    def is_accept(self) -> bool:
        return self.current_state.is_accept

    def is_reject(self) -> bool:
        return self.current_state.is_reject

    def has_timed_out(self) -> bool:
        return self.step_count >= self.max_steps

    def display_configuration(self) -> None:

        tape_string, start_position = self.tape.render(self.head.position)

        symbols = tape_string.split()

        print(f"Step: {self.step_count}")
        print(f"State: {self.current_state.name}")
        print()

        print("Index:")

        indices = " ".join(
            str(i) for i in range(start_position, start_position + len(symbols))
        )

        print(indices)

        print("Tape:")
        print(tape_string)

        head_offset = self.head.position - start_position

        pointer = []

        for i in range(len(symbols)):

            if i == head_offset:
                pointer.append("^")

            else:
                pointer.append(" ")

        print(" ".join(pointer))
        print()

        print(f"Head Position: {self.head.position}")

        print("-" * 40)

    def get_status(self) -> str | None:

        if self.is_accept():
            return ACCEPT

        if self.is_reject():
            return REJECT

        if self.has_timed_out():
            return TIMEOUT

        return None

    def run(self) -> str:

        while True:

            self.display_configuration()

            status = self.get_status()

            if status is not None:

                print(f"Machine {status}.")

                return status

            if not self.step():

                print("No valid transition found.")

                print("Machine Rejected.")

                return REJECT
