## Operation Tests
## Evan Garvey
## IS 601, Module 3

import pytest # type: ignore
from app.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, expected", [
    (1.0, 2.0, 3.0),
    (-5.0, 5.0, 0.0),
    (2.5, 2.5, 5.0),
])
def test_add(a, b, expected):
    assert add(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("a, b, expected", [
    (5.0, 3.0, 2.0),
    (-5.0, -5.0, 0.0),
    (2.5, 5.0, -2.5),  
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("a, b, expected", [
    (2.0, 3.0, 6.0),
    (-1.5, 4.0, -6.0),
    (0.0, 10.0, 0.0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("a, b, expected", [
    (6.0, 3.0, 2.0),
    (10.0, 2.5, 4.0),
    (-9.0, 3.0, -3.0),
])
def test_divide(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)