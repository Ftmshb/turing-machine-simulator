from simulator.tape import Tape
from simulator.head import Head

from simulator.constants import ACCEPT, REJECT, TIMEOUT


class UniversalTM:
    """
    Universal Turing Machine.

    Simulates another Turing Machine using:
    - RuleScanner
    - Tape
    - Head
    """

    def __init__(
        self,
        scanner,
        input_string,
        start_state,
        accept_state,
        reject_state,
        max_steps=500,
    ):

        self.scanner = scanner

        self.tape = Tape(input_string=input_string, blank_symbol="_")

        self.head = Head()

        self.current_state = start_state

        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state

        self.max_steps = max_steps
        self.step_count = 0

    def get_current_symbol(self):
        """
        Read symbol under head.
        """

        return self.tape.read(self.head.position)

    def execute_rule(self, rule):
        """
        Execute one transition rule.
        """

        # write
        self.tape.write(self.head.position, rule.write_symbol)

        # move
        self.head.move(rule.direction)

        # change state
        self.current_state = rule.next_state

        self.step_count += 1

    def is_accept(self):

        return self.current_state == self.accept_state

    def is_reject(self):

        return self.current_state == self.reject_state

    def is_timeout(self):

        return self.step_count >= self.max_steps

    def get_status(self):

        if self.is_accept():
            return ACCEPT

        if self.is_reject():
            return REJECT

        if self.is_timeout():
            return TIMEOUT

        return None

    def step(self):
        """
        Perform one simulation step.
        """

        symbol = self.get_current_symbol()

        rule = self.scanner.find_rule(self.current_state, symbol)

        if rule is None:
            return False

        self.execute_rule(rule)

        return True

    def display_configuration(self):

        tape_string, start = self.tape.render(self.head.position)

        symbols = tape_string.split()

        print("=" * 40)

        print(f"Step: {self.step_count}")

        print(f"State: {self.current_state}")

        print()

        print("Tape:")

        print(tape_string)

        print()

        pointer = []

        head_index = self.head.position - start

        for i in range(len(symbols)):

            if i == head_index:
                pointer.append("^")
            else:
                pointer.append(" ")

        print(" ".join(pointer))

        print(f"Head: {self.head.position}")

        print("=" * 40)

    def run(self):

        while True:

            self.display_configuration()

            status = self.get_status()

            if status is not None:

                print(f"Machine {status}")

                return status

            if not self.step():

                print("No transition found.")

                print("Machine REJECT")

                return REJECT
