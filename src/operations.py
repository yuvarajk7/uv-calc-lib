"""Calculation operation module contains add, subtract, multiply, divide"""


def add(a: int, b: int) -> int:
    """Add two numbers
    Args:
        a: first number
        b: second number

    Returns:
        The sum of a and b
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract two numbers
    Args:
        a: first number
        b: second number

    Returns:
        The difference of a and b
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers
    Args:
        a: first number
        b: second number

    Returns:
        The multiple of a and b
    """
    return a * b


def divide(a: int, b: int) -> float:
    """Divide two numbers
    Args:
        a: first number
        b: second number

    Returns:
        The divide of a and b

    Raises:
            ZeroDivisionError: if b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b