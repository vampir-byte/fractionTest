from fraction import Fraction
import unittest

class test_fraction_add(unittest.TestCase):
  # Tests adding with fractions of same denominator.
  def test_add(self):
    a = Fraction(1, 4)
    b = Fraction(2, 4)
    result = a.add(b)
    self.assertEqual(result.numerator, 3)
    self.assertEqual(result.denominator, 4)
  # Tests adding with fraction of different denominators.
  def test_add_diff_den(self):
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    result = a.add(b)
    self.assertEqual(result.numerator, 5)
    self.assertEqual(result.denominator, 6)
  # Tests adding with fraction and an int.
  def test_add_int(self):
    a = Fraction(1, 2)
    b = 2
    result = a.add(b)
    self.assertEqual(result.numerator, 5)
    self.assertEqual(result.denominator, 2)
  # Tests adding with incorrect type float
  def test_add_float_exception(self):
    a = Fraction(1, 2)
    b = 1.4444
    with self.assertRaises(TypeError):
      result = a.add(b)
  # Tests adding with incorrect type String
  def test_add_string_exception(self):
    a = Fraction(1, 2)
    b = "Hello World!"
    with self.assertRaises(TypeError):
      result = a.add(b)
