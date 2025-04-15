import unittest
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

def test_multiply(self):
    self.assertEqual(calculator.mul(2, 3), 6)
    self.assertEqual(calculator.mul(-1, 5), -5)
    self.assertEqual(calculator.mul(-2, -3), 6)
    self.assertEqual(calculator.mul(0, 5), 0)

def test_divide(self):
    self.assertEqual(calculator.div(2, 10), 5)
    self.assertEqual(calculator.div(4, -8), -2)
    self.assertAlmostEqual(calculator.div(3, 1), 0.3333333333333333)

def test_log_invalid_argument(self):
    with self.assertRaises(ValueError):
        calculator.log(2, -1)
    with self.assertRaises(ValueError):
        calculator.log(-2, 10)

def test_hypotenuse(self):
    self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
    self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)
    self.assertAlmostEqual(calculator.hypotenuse(1, 1), math.sqrt(2))
    self.assertEqual(calculator.hypotenuse(0, 0), 0)

def test_sqrt(self):
    self.assertEqual(calculator.sqrt(4), 2)
    self.assertEqual(calculator.sqrt(9), 3)
    self.assertAlmostEqual(calculator.sqrt(2), 1.4142135623730951)
    with self.assertRaises(ValueError):
        calculator.sqrt(-1)

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