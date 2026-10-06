from fraction import Fraction
import unittest

class test_fraction_add(unittest.TestCase):
  def test_add(self):
    a = Fraction(1/4)
    b = Fraction(2/4)
    a.add(b)
  def test_add_diff_dom(self):
    a = Fraction(1/2)
    b = Fraction(1/3)
    a.add(b)
