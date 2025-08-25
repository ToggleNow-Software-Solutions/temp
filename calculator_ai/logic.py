from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> float:
    """Return a + b as float."""
    return float(a) + float(b)


def subtract(a: Number, b: Number) -> float:
    """Return a - b as float."""
    return float(a) - float(b)
