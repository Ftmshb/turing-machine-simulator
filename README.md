# Turing Machine Simulator

## Project Description

This project is a deterministic single-tape Turing Machine simulator developed in Python for the Automata Theory course.

The simulator loads a Turing Machine definition from a JSON file, executes it on an input string, and displays the execution step by step until the machine reaches an Accept or Reject state.

---

## Technologies

- Python 3
- JSON

---

## Project Structure

```
project/
│
├── main.py
├── machines/
│   └── copy_machine.json
├── simulator/
│   ├── constants.py
│   ├── head.py
│   ├── parser.py
│   ├── state.py
│   ├── tape.py
│   ├── transition.py
│   └── turing_machine.py
└── tests/
    ├── invalid01_invalid_symbol.txt
    ├── invalid02_missing_S.txt
    └── ...
```

---

## Requirements

- Python 3.10 or newer

No external libraries are required.

---

## How to Run

Open a terminal in the project directory and run:

```bash
python main.py
```

When prompted, enter the name of an input file located in the `tests` folder.

Example:

```text
Enter test file name (e.g. test1.txt): test1.txt
```

---

## Machine Description

The Turing Machine is described in:

```
machines/copy_machine.json
```

This file contains:

- States
- Input alphabet
- Tape alphabet
- Blank symbol
- Start state
- Accept state
- Reject state
- Transition function

The simulator parses this file and constructs the Turing Machine dynamically before execution.

---

## Sample Input

Example test file (`tests/invalid02_missing_S.txt`):

```text
10#XX_G
```

---

## Sample Output

```text
Enter test file name (e.g. test1.txt): invalid02_missing_S.txt

Step: 0
State: qStart

...

No valid transition found.
Machine Rejected.
```

---

## Notes

- The simulator executes one transition at a time.
- At each step, it displays the current state, tape contents, head position, and executed transition.
- If no valid transition exists for the current state and symbol, the machine halts and rejects the input.

---

## Authors

Automata Theory Course Project