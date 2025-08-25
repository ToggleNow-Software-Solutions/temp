from calculator_ai.logic import add, subtract


def test_add():
    assert add(2, 3) == 5.0
    assert add(-1, 1.5) == 0.5


def test_subtract():
    assert subtract(5, 2) == 3.0
    assert subtract(-1, -2) == 1.0
