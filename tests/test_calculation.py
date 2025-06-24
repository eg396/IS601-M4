## Test_calculation.py
## Evan Garvey
## IS 601, Module 4

## Since my test_calculator covers a large percentage of the calculations file, I will be only testing edge cases here

import pytest # type: ignore
from app.calculation import CalculationFactory, AddCalculation, SubtractCalculation, MultiplyCalculation, DivideCalculation, Calculation
from app.operations import Operations

def test_calculation_repr_addition():

    ## Test that the calculation representation is correct
    ## runs the repr function on an addition calculation

    num1, num2 = 1.0, 2.0
    add_calc = AddCalculation(num1, num2)
    calc_repr = repr(add_calc)

    expected_repr = f"{AddCalculation.__name__}(num1 = {num1}, num2 = {num2})"

    assert calc_repr == expected_repr

def test_calculation_repr_subtraction():

    ## Test that the calculation representation is correct
    ## runs the repr function on a subtraction calculation

    num1, num2 = 1.0, 2.0
    sub_calc = SubtractCalculation(num1, num2)
    calc_repr = repr(sub_calc)

    expected_repr = f"{SubtractCalculation.__name__}(num1 = {num1}, num2 = {num2})"

    assert calc_repr == expected_repr

def test_calculation_repr_multiplication():

    ## Test that the calculation representation is correct
    ## runs the repr function on a multiplication calculation

    num1, num2 = 1.0, 2.0
    mul_calc = MultiplyCalculation(num1, num2)
    calc_repr = repr(mul_calc)

    expected_repr = f"{MultiplyCalculation.__name__}(num1 = {num1}, num2 = {num2})"

    assert calc_repr == expected_repr

def test_calculation_repr_division():

    ## Test that the calculation representation is correct
    ## runs the repr function on a division calculation

    num1, num2 = 1.0, 2.0
    div_calc = DivideCalculation(num1, num2)
    calc_repr = repr(div_calc)

    expected_repr = f"{DivideCalculation.__name__}(num1 = {num1}, num2 = {num2})"

    assert calc_repr == expected_repr

def test_factory_duplicate_register_handling():

    ## Test that the factory handles duplicate registration
    ## runs the register_calculation function twice, the second one being a duplicate add calculation

    with pytest.raises(ValueError) as exc_info:
        @CalculationFactory.register_calculation("add")
        class DuplicateAddCalculation(Calculation):

            def execute(self) -> float:

                return Operations.add(self.num1, self.num2)

    assert "Calculation type 'add' is already registered." in str(exc_info.value)