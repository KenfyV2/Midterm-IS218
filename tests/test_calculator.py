import pytest
from app.calculator import Calculator

def test_add():
    assert Calculator.add(1, 2) == 3
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(-1, -1) == -2

def test_subtract():
    assert Calculator.subtract(2, 1) == 1
    assert Calculator.subtract(2, 2) == 0
    assert Calculator.subtract(-1, -1) == 0

def test_multiply():
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(-1, 1) == -1
    assert Calculator.multiply(-1, -1) == 1

def test_divide():
    assert Calculator.divide(6, 3) == 2
    assert Calculator.divide(-1, 1) == -1
    assert Calculator.divide(-1, -1) == 1
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)