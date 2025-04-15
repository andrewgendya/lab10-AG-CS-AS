import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def logarithm(base, value):
    if base <= 0 or base == 1 or value <= 0:
        raise ValueError("Invalid arguments for logarithm")
    return math.log(value, base)

def hypotenuse(a, b):
    return math.sqrt(a*a + b*b)

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x)