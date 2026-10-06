import unittest
import sys
import os

# Add the parent directory to the path to import Fraction
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fraction import Fraction


class TestFractionMultiplication(unittest.TestCase):
    """Test cases for Fraction multiplication (__mul__ method)."""

    def test_multiply_two_fractions_basic(self):
        """Test basic multiplication of two fractions."""
        frac1 = Fraction(2, 3)
        frac2 = Fraction(3, 4)
        result = frac1 * frac2
        # (2/3) * (3/4) = 6/12 = 1/2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)

    def test_multiply_fraction_by_integer(self):
        """Test multiplication of a fraction by an integer."""
        frac = Fraction(2, 3)
        result = frac * 4
        # (2/3) * 4 = 8/3
        self.assertEqual(result.numerator, 8)
        self.assertEqual(result.denominator, 3)

    def test_multiply_integer_by_fraction(self):
        """Test multiplication of an integer by a fraction."""
        frac = Fraction(3, 5)
        result = 3 * frac
        # 3 * (3/5) = 9/5
        self.assertEqual(result.numerator, 9)
        self.assertEqual(result.denominator, 5)

    def test_multiply_fraction_by_zero(self):
        """Test multiplication of a fraction by zero."""
        frac = Fraction(5, 7)
        result = frac * 0
        # (5/7) * 0 = 0/1
        self.assertEqual(result.numerator, 0)
        self.assertEqual(result.denominator, 1)

    def test_multiply_zero_fraction_by_number(self):
        """Test multiplication of zero fraction by a number."""
        frac = Fraction(0, 1)
        result = frac * 10
        # 0 * 10 = 0/1
        self.assertEqual(result.numerator, 0)
        self.assertEqual(result.denominator, 1)

    def test_multiply_by_one(self):
        """Test multiplication of a fraction by one."""
        frac = Fraction(7, 11)
        result = frac * 1
        # (7/11) * 1 = 7/11
        self.assertEqual(result.numerator, 7)
        self.assertEqual(result.denominator, 11)

    def test_multiply_by_negative_fraction(self):
        """Test multiplication by a negative fraction."""
        frac = Fraction(2, 3)
        frac_neg = Fraction(-1, 2)
        result = frac * frac_neg
        # (2/3) * (-1/2) = -2/6 = -1/3
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 3)

    def test_multiply_by_negative_integer(self):
        """Test multiplication by a negative integer."""
        frac = Fraction(3, 4)
        result = frac * (-2)
        # (3/4) * (-2) = -6/4 = -3/2
        self.assertEqual(result.numerator, -3)
        self.assertEqual(result.denominator, 2)

    def test_multiply_two_negative_fractions(self):
        """Test multiplication of two negative fractions."""
        frac1 = Fraction(-2, 3)
        frac2 = Fraction(-3, 4)
        result = frac1 * frac2
        # (-2/3) * (-3/4) = 6/12 = 1/2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)

    def test_multiply_results_in_normalization(self):
        """Test that multiplication result is normalized to lowest terms."""
        frac1 = Fraction(2, 6)  # Should normalize to 1/3
        frac2 = Fraction(3, 4)
        result = frac1 * frac2
        # (1/3) * (3/4) = 3/12 = 1/4
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 4)

    def test_multiply_larger_fractions(self):
        """Test multiplication of larger fractions."""
        frac1 = Fraction(15, 20)  # Normalizes to 3/4
        frac2 = Fraction(8, 10)   # Normalizes to 4/5
        result = frac1 * frac2
        # (3/4) * (4/5) = 12/20 = 3/5
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 5)

    def test_multiply_unit_fractions(self):
        """Test multiplication of unit fractions."""
        frac1 = Fraction(1, 2)
        frac2 = Fraction(1, 3)
        result = frac1 * frac2
        # (1/2) * (1/3) = 1/6
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

    def test_multiply_identical_fractions(self):
        """Test multiplication of identical fractions."""
        frac = Fraction(3, 5)
        result = frac * frac
        # (3/5) * (3/5) = 9/25
        self.assertEqual(result.numerator, 9)
        self.assertEqual(result.denominator, 25)

    def test_multiply_reciprocals(self):
        """Test multiplication of reciprocal fractions."""
        frac1 = Fraction(2, 5)
        frac2 = Fraction(5, 2)
        result = frac1 * frac2
        # (2/5) * (5/2) = 10/10 = 1/1
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

    def test_multiply_does_not_modify_operands(self):
        """Test that multiplication does not modify the original fractions."""
        frac1 = Fraction(2, 3)
        frac2 = Fraction(3, 4)
        original_num1, original_den1 = frac1.numerator, frac1.denominator
        original_num2, original_den2 = frac2.numerator, frac2.denominator
        
        result = frac1 * frac2
        
        # Verify operands were not modified
        self.assertEqual(frac1.numerator, original_num1)
        self.assertEqual(frac1.denominator, original_den1)
        self.assertEqual(frac2.numerator, original_num2)
        self.assertEqual(frac2.denominator, original_den2)

    def test_multiply_type_error_with_string(self):
        """Test that TypeError is raised when multiplying by string."""
        frac = Fraction(2, 3)
        with self.assertRaises(TypeError):
            result = frac * "2"

    def test_multiply_type_error_with_list(self):
        """Test that TypeError is raised when multiplying by list."""
        frac = Fraction(2, 3)
        with self.assertRaises(TypeError):
            result = frac * [2, 3]

    def test_multiply_fraction_by_float(self):
        """Test multiplication of a fraction by a float (unsupported type)."""
        frac = Fraction(2, 3)
        with self.assertRaises(TypeError):
            result = frac * 2.5

    def test_multiply_chain_operations(self):
        """Test chaining multiple multiplications."""
        frac1 = Fraction(1, 2)
        frac2 = Fraction(2, 3)
        frac3 = Fraction(3, 4)
        result = frac1 * frac2 * frac3
        # (1/2) * (2/3) * (3/4) = 6/24 = 1/4
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 4)

    def test_multiply_with_one_denominator(self):
        """Test multiplication when fractions have denominator 1 (integers)."""
        frac1 = Fraction(5, 1)
        frac2 = Fraction(3, 1)
        result = frac1 * frac2
        # 5 * 3 = 15/1
        self.assertEqual(result.numerator, 15)
        self.assertEqual(result.denominator, 1)

    def test_multiply_fraction_by_negative_one(self):
        """Test multiplication by negative one."""
        frac = Fraction(7, 9)
        result = frac * (-1)
        # (7/9) * (-1) = -7/9
        self.assertEqual(result.numerator, -7)
        self.assertEqual(result.denominator, 9)


if __name__ == '__main__':
    unittest.main()
