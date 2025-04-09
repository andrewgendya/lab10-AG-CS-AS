import calculator
import math

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    assert calculator.sub(5, 3) == 2
    assert calculator.sub(0, 0) == 0
    assert calculator.sub(-2, -4) == 2

def test_divide_by_zero():
    try:
        calculator.div(0, 10)
        print("test_divide_by_zero FAILED (no exception)")
    except ZeroDivisionError:
        print("test_divide_by_zero passed")

def test_logarithm():
    assert math.isclose(calculator.log(2, 8), 3)
    assert math.isclose(calculator.log(10, 100), 2)

def test_log_invalid_base():
    for a, b in [(1, 10), (-2, 10), (2, -10)]:
        try:
            calculator.log(a, b)
            print(f"test_log_invalid_base FAILED (a={a}, b={b})")
        except ValueError:
            print(f"test_log_invalid_base passed (a={a}, b={b})")

def run_all_tests():
    try:
        test_add()
        print("test_add passed")
    except AssertionError:
        print("test_add FAILED")

    try:
        test_subtract()
        print("test_subtract passed")
    except AssertionError:
        print("test_subtract FAILED")

    test_divide_by_zero()

    try:
        test_logarithm()
        print("test_logarithm passed")
    except AssertionError:
        print("test_logarithm FAILED")

    test_log_invalid_base()

if __name__ == "__main__":
    run_all_tests()
