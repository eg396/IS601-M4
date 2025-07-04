## Interface Tests
## Evan Garvey
## IS 601, Module 4

import sys
import textwrap
import pytest # type: ignore
from io import StringIO
from app.calculator import calculator, display_help, display_history

## Tests

def test_display_help(capsys):

    ## Test that help is displayed properly
    ## Runs the help function and captures the output, then compares to expectation

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
        exit: Exit the calculator

    Examples: 
        add 1 2
        subtract 1 2
        multiply 1 2
        divide 1 2
    """
    assert capture.out.strip() == expected_output.strip()

def test_display_history_empty(capsys):

    ## Test that history is displayed properly
    ## Runs the history function and captures the output, then checks if it is empty

    history = []

    display_history(history)

    capture = capsys.readouterr()
    assert capture.out.strip() == "Error: No calculations in history."

def test_display_history_nonempty(capsys):

    ## Test that history is displayed properly
    ## Runs the history function and captures the output, then compares to expectation

    history = [
        "AddCalculation: 15.0 add 5.0 = 20.0",
        "SubtractCalculation: 20.0 subtract 5.0 = 15.0",
        "MultiplyCalculation: 15.0 multiply 5.0 = 75.0",
        "DivideCalculation: 75.0 divide 5.0 = 15.0"
    ]

    display_history(history)

    capture = capsys.readouterr()
    expected_output = textwrap.dedent("""\
    Calculation History:
    1. AddCalculation: 15.0 add 5.0 = 20.0
    2. SubtractCalculation: 20.0 subtract 5.0 = 15.0
    3. MultiplyCalculation: 15.0 multiply 5.0 = 75.0
    4. DivideCalculation: 75.0 divide 5.0 = 15.0""")

    assert capture.out.strip() == expected_output.strip()

def test_calculator_quit(monkeypatch, capsys):

    ## Test that the calculator exits properly
    ## Runs the calculator using the 'exit' command

    user_input = 'exit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 0

def test_calculator_help_command(monkeypatch, capsys):

    ## Test that the calculator displays help properly
    ## Runs the calculator using the 'help' command

    user_input = 'help\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "REPL Calculator help" in captured.out
    assert "Goodbye!" in captured.out

def test_calculator_invalid_input(monkeypatch, capsys):

    ## Test that the calculator displays the 'invalid input' user message properly
    ## Runs the calculator using invalid input

    user_input = 'invalid input\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "Invalid parameters. Parameters 2 and 3 must be valid floats. Please try again." in captured.out
    assert "Type 'help' for more information." in captured.out

def test_calculator_addition(monkeypatch, capsys):

    ## Test that the calculator performs addition properly
    ## Runs the calculator using the 'add' command

    user_input = 'add 1 2\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "result: AddCalculation: 1.0 Add 2.0 = 3.0" in captured.out

def test_calculator_subtraction(monkeypatch, capsys):

    ## Test that the calculator performs subtraction properly
    ## Runs the calculator using the 'subtract' command

    user_input = 'subtract 1 2\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "result: SubtractCalculation: 1.0 Subtract 2.0 = -1.0" in captured.out

def test_calculator_multiplication(monkeypatch, capsys):

    ## Test that the calculator performs multiplication properly
    ## Runs the calculator using the 'multiply' command

    user_input = 'multiply 1 2\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "result: MultiplyCalculation: 1.0 Multiply 2.0 = 2.0" in captured.out

def test_calculator_division(monkeypatch, capsys):

    ## Test that the calculator performs division properly
    ## Runs the calculator using the 'divide' command

    user_input = 'divide 1 2\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "result: DivideCalculation: 1.0 Divide 2.0 = 0.5" in captured.out

def test_calculator_division_by_zero(monkeypatch, capsys):

    ## Test that the calculator handles division by zero properly
    ## Runs the calculator using the 'divide' command with zero as the divisor

    user_input = 'divide 1 0\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "error occurred: Division by zero is not allowed." in captured.out

def test_calculator_invalid_operation(monkeypatch, capsys):

    ## Test that the calculator handles invalid operations properly
    ## Runs the calculator using an invalid operation

    user_input = 'invalid_operation 1 2\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "Invalid calculation type: invalid_operation. Available types: add, subtract, multiply, divide" in captured.out

def test_calculator_test_history(monkeypatch, capsys):

    ## Test that the calculator correctly displays history
    ## Runs the calculator using several math operations and then the 'history' command

    user_input = 'add 1 2\nsubtract 1 2\nhistory\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "result: AddCalculation: 1.0 Add 2.0 = 3.0" in captured.out
    assert "result: SubtractCalculation: 1.0 Subtract 2.0 = -1.0" in captured.out
    assert "Calculation History:" in captured.out
    assert "1. AddCalculation: 1.0 Add 2.0 = 3.0" in captured.out
    assert "2. SubtractCalculation: 1.0 Subtract 2.0 = -1.0" in captured.out

def test_calculator_keyboard_interrupt(monkeypatch, capsys):

    ## Test that the calculator handles keyboard interrupts properly
    ## Runs the calculator using a mock keyboard interrupt

    def mock_input(prompt):

        raise KeyboardInterrupt()
    
    monkeypatch.setattr('builtins.input', mock_input)

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "Keyboard Interrupt detected. Goodbye!" in captured.out
    assert exc_info.value.code == 0

def test_calculator_eof_error(monkeypatch, capsys):

    ## Test that the calculator handles EOF errors properly
    ## Runs the calculator using a mock EOF error

    def mock_input(prompt):

        raise EOFError()
    
    monkeypatch.setattr('builtins.input', mock_input)

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "EOF detected. Goodbye!" in captured.out
    assert exc_info.value.code == 0