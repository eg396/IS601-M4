## Interface Tests
## Evan Garvey
## IS 601, Module 4

import sys
from io import StringIO
from app.calculator import calculator, display_help, display_history

## Monkeypatch for input handling

def run_calculator_with_input(monkeypatch, inputs):
    iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(iterator))
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()

## Tests

def test_display_help(capsys):

    display_help()
    capture = capsys.readouterr()
    expected_output = """
    REPL Calculator help
          
    Usage:
        <operation> <num1> <num2>
        Perform a specified operation on two submitted numbers.
        Supported operations: 
            add: adds two numbers
            subtract: subtracts two numbers
            multiply: multiplies two numbers
            divide: divides two numbers

    Special Commands:
        help: Display this message
        history: Display the command history
        quit: Exit the calculator

    Examples: 
        add 1 2
        subtract 1 2
        multiply 1 2
        divide 1 2
    """
    assert capture.out.strip() == expected_output.strip()

def test_display_history_empty(capsys):

    history = []

    display_history(history)

    capture = capsys.readouterr()
    assert capture.out.strip() == "Error: No calculations in history."

def test_display_history_nonempty(capsys):

    history = [
        "AddCalculation: 15.0 add 5.0 = 20.0",
        "SubtractCalculation: 20.0 subtract 5.0 = 15.0",
        "MultiplyCalculation: 15.0 multiply 5.0 = 75.0",
        "DivideCalculation: 75.0 divide 5.0 = 15.0"
    ]

    display_history(history)

    capture = capsys.readouterr()
    assert capture.out.strip() == """
    Calculation History:
    1. AddCalculation: 15.0 add 5.0 = 20.0
    2. SubtractCalculation: 20.0 subtract 5.0 = 15.0
    3. MultiplyCalculation: 15.0 multiply 5.0 = 75.0
    4. DivideCalculation: 75.0 divide 5.0 = 15.0""".strip()

