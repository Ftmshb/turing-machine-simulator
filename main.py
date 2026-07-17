from simulator.parser import Parser
from simulator.tape import Tape
from simulator.head import Head
from simulator.turing_machine import TuringMachine

JSON_PATH = "machines/copy_machine.json"


def load_input(file_path: str) -> str:
    """Load the initial tape from a text file."""

    with open(file_path, "r", encoding="utf-8") as input_file:
        return input_file.read().strip()


def main():
    """Run the Turing Machine simulator."""

    while True:

        try:
            test_file = input("Enter test file name (e.g. test1.txt): ").strip()

            input_path = f"tests/{test_file}"

            parser = Parser(JSON_PATH)

            (
                states,
                transitions,
                start_state,
                input_alphabet,
                tape_alphabet,
            ) = parser.parse_machine()

            input_string = load_input(input_path)

            tape = Tape(
                input_string=input_string,
                blank_symbol=parser.blank_symbol,
            )

            head = Head()

            machine = TuringMachine(
                states=states,
                transitions=transitions,
                start_state=start_state,
                tape=tape,
                head=head,
                input_alphabet=input_alphabet,
                tape_alphabet=tape_alphabet,
            )

            machine.run()

        except FileNotFoundError:
            print("\nError: Input file not found.")

        except ValueError as error:
            print(f"\nError: {error}")

        except Exception as error:
            print(f"\nUnexpected error: {error}")

        choice = input("\nRun another test? (y/n): ").strip().lower()

        if choice != "y":
            print("Turing Machine Simulator closed.")
            break


if __name__ == "__main__":
    main()
