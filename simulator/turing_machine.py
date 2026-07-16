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

    This class coordinates the tape, head, states and transitions,
    and executes the machine step by step.
    """

    def __init__(
        self,
        states: dict[str, State],
        transitions: dict[tuple[str, str], Transition],
        start_state: State,
        tape: Tape,
        head: Head,
        max_steps: int = DEFAULT_MAX_STEPS,
    ):
        """
        Initialize the Turing Machine.

        Args:
            states: Dictionary of all machine states.
            transitions: Dictionary of transition rules.
            start_state: Initial state.
            tape: Machine tape.
            head: Machine head.
            max_steps: Maximum allowed execution steps.
        """
        if max_steps <= 0:
            raise ValueError("max_steps must be greater than zero.")

        if start_state.name not in states:
            raise ValueError("Start state must exist in states.")

        for transition in transitions.values():
            if transition.next_state not in states:
                raise ValueError(f"Undefined next state: {transition.next_state}")

        self.states = states
        self.transitions = transitions

        self.current_state = start_state

        self.tape = tape
        self.head = head

        self.max_steps = max_steps
        self.step_count = 0

    def get_current_symbol(self) -> str:
        """
        Return the symbol currently under the head.
        """

        return self.tape.read(self.head.position)

    def find_transition(self) -> Transition | None:
        """
        Find the transition that matches the current state
        and current tape symbol.
        """

        key = (
            self.current_state.name,
            self.get_current_symbol(),
        )

        return self.transitions.get(key)

    def step(self) -> bool:
        """
        Execute one transition.

        Returns:
            True if a transition was executed.
            False if no transition exists.
        """

        transition = self.find_transition()

        if transition is None:
            return False

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
        """
        Return True if the machine is in an accept state.
        """

        return self.current_state.is_accept

    def is_reject(self) -> bool:
        """
        Return True if the machine is in a reject state.
        """

        return self.current_state.is_reject

    def has_timed_out(self) -> bool:
        """
        Check whether the machine exceeded
        the maximum number of execution steps.
        """

        return self.step_count >= self.max_steps

    def display_configuration(self) -> None:
        """
        Display the current machine configuration.
        """

        tape_string, start_position = self.tape.render(self.head.position)

        symbols = tape_string.split()

        print(f"Step: {self.step_count}")
        print(f"State: {self.current_state.name}")
        print()

        # Print tape indices
        print("Index:")
        indices = " ".join(
            str(i) for i in range(start_position, start_position + len(symbols))
        )
        print(indices)

        # Print tape symbols
        print("Tape:")
        print(tape_string)

        # Print head pointer
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
        """
        Return the current machine status.

        Returns:
            ACCEPT, REJECT, TIMEOUT or None if execution should continue.
        """

        if self.is_accept():
            return ACCEPT

        if self.is_reject():
            return REJECT

        if self.has_timed_out():
            return TIMEOUT

        return None

    def run(self) -> str:
        """
        Run the machine until it halts.
        """

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
