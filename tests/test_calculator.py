## Interface Tests
## Evan Garvey
## IS 601, Module 4

import sys
from io import StringIO
from app.calculator import calculator, is_float

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

def test_addition(monkeypatch):
    inputs = ['add 1 2', 'quit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 3.0" in output

def test_subtraction(monkeypatch):
    inputs = ['subtract 1 2', 'quit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: -1.0" in output

def test_multiplication(monkeypatch):
    inputs = ['multiply 2 3', 'quit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 6.0" in output

def test_division(monkeypatch):
    inputs = ['divide 10 2', 'quit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output

def test_division_by_zero(monkeypatch):
    inputs = ['divide 10 0', 'quit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Cannot divide by zero. Please try again." in output

def test_invalid_operation(monkeypatch):
    inputs = ['exponent 1 2', 'quit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid operation. Please try again." in output

def test_invalid_parameter_count(monkeypatch):
    inputs = ['add 1', 'quit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid parameters. 3 Parameters are required (operation, num1, num2). Please try again." in output

def test_invalid_floats(monkeypatch):
    inputs = ['add one 2', 'quit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid parameters. Parameters 2 and 3 must be valid floats. Please try again." in output

def test_exit(monkeypatch):
    inputs = ['quit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Goodbye!" in output

## Helper function tests for is_float

def test_is_float():
    assert is_float('1')

def test_is_negative_float():
    assert is_float('-1')

def test_is_not_float():
    assert not is_float('1.1.1')