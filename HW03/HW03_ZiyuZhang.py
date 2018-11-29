# Coded by ZiyuZhang
# Fraction calculator
import unittest


class Fraction:
    """
        This class represents a object of fractions including its calculations.
        There are no member fuctions(methods):
        but 2 members(attributes):
        numerator
        denominator
        and 2 magics:
        __init__: constructor
        __str__: transfer 1 class to string so that we can use print() to output
    """
    __slots__ = {'numerator', 'denominator'}

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator == 0:
            raise ZeroDivisionError('Your denominator equals to zero, plz check your input. \n')

    """
    def Simplify(frac):
        a = GCD(frac.numerator, frac.denominator)
        return Fraction(frac.numerator / a, frac.denominator / a)
    """

    """
    def GCD(a, b):
    """

    def __str__(self):
        FracStr = str(self.numerator) + ' / ' + str(self.denominator)
        return FracStr

    def __add__(self, other):
        num = self.numerator * other.denominator + self.denominator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.numerator * other.denominator - self.denominator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError('Divisor equals to zero. \n')
        else:
            num = self.numerator * other.denominator
            den = self.denominator * other.numerator
            return Fraction(num, den)

    def __eq__(self, other):
        prod_1 = self.numerator * other.denominator
        prod_2 = self.denominator * other.numerator
        return prod_1 == prod_2

    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True

    def __lt__(self, other):
        diff = self - other
        if diff.numerator < 0 or diff.denominator < 0:
            return True
        else:
            return False

    def __le__(self, other):
        diff = self - other
        if diff.numerator <= 0 or diff.denominator <= 0:
            return True
        else:
            return False

    def __gt__(self, other):
        if self <= other:
            return False
        else:
            return True

    def __ge__(self, other):
        if self < other:
            return False
        else:
            return True


class FractionTest(unittest.TestCase):
    def test_init(self):
        case = Fraction(1, 2)
        self.assertEqual(case.numerator, 1)
        self.assertEqual(case.denominator, 2)

    def test_raise(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

    def test_add(self):
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        case_3 = Fraction(1, 4)
        self.assertEqual((case_1 + case_2), Fraction(5, 6))
        self.assertEqual(case_1 + case_2 + case_3, Fraction(13, 12))

    def test_sub(self):
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        self.assertEqual((case_1 - case_2), Fraction(1, 6))

    def test_mul(self):
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        self.assertEqual(case_1 * case_2, Fraction(1, 6))

    def test_divide(self):
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        self.assertEqual(case_1 / case_2, Fraction(3, 2))

    def test_ne(self):
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        self.assertEqual(case_1 != case_1, False)
        self.assertEqual(case_1 != case_2, True)

    def test_lt(self):
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        self.assertEqual(case_1 < case_1, False)
        self.assertEqual(case_1 < case_2, False)
        self.assertEqual(case_2 < case_1, True)

    def test_le(self):
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        self.assertEqual(case_1 <= case_1, True)
        self.assertEqual(case_1 <= case_2, False)
        self.assertEqual(case_2 <= case_1, True)

    def test_gt(self):
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        self.assertEqual(case_1 > case_1, False)
        self.assertEqual(case_1 > case_2, True)
        self.assertEqual(case_2 > case_2, False)

    def test_ge(self):
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        self.assertEqual(case_1 >= case_1, True)
        self.assertEqual(case_1 >= case_2, True)
        self.assertEqual(case_2 >= case_1, False)


def getInput():
    try:
        Num_1 = input('Input fraction 1 numerator: ')
        Den_1 = input('Input fraction 1 denominator: ')
        return Fraction(float(Num_1), float(Den_1))
    except ZeroDivisionError as z:
        print(z)


def UserDoing():
    """
        Modifying is always good
    """
    print('Input 2 fractions')
    Frac_1 = getInput()
    Operator = input("Input operator(+, -, *, /): ")
    Frac_2 = getInput()
    OpDic = {'+': (Frac_1 + Frac_2), '-': (Frac_1 - Frac_2), '*': (Frac_1 * Frac_2), '/': (Frac_1 / Frac_2), '=': (Frac_1 == Frac_2)}
    return OpDic[Operator]


def main():
    """
        main function. In this section. We will invoke test()
        and we will let users to do some operations of fractions with UserDoing()
    """
    print('Main function started. \n')
    Q = 'PYTHON'
    while Q != 'Q' and Q != 'q':
        print(UserDoing())
        Q = input('Input any characters except Q/q to continue: ')

    print('Main function ended. \n')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()
