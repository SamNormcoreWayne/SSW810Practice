# Coded by ZiyuZhang
# Fraction calculator
# THIS IS HOMEWORK 4.3!!!
# Plz focus on line 11, line 87 and line 233!
# I rewrite __eq__()
# Fraction(k*a, k*b).Simplify() == Fraction(a, b) can be proved when I invoke __eq__()
# But also, for your confusion, I use self.assertEqual(Fraction(2, 4).Simplify(), Fraction(1, 2)) to explain my theory
import unittest


def GCD(a, b):
    a = abs(a)
    b = abs(b)
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


class Fraction:
    """
        This class represents a object of fractions including its calculations.
        There are no member fuctions(methods):
        but 2 members(attributes):
        numerator
        denominator
        and many magic methods:
        __init__: constructor
        __str__: transfer 1 class to string so that we can use print() to output
        __add__: implement fraction plus
        __minus__: implement fraction subtraction
        __mul__: implement fraction multiply
        __truediv__: implement fraction division
        __eq__: ==
        __ne__: !=
        __lt__: <
        __le__: <=
        __gt__: >
        __ge__: >=
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
        frac_1 = self.Simplify()
        frac_2 = other.Simplify()
        if abs(frac_1.numerator) == abs(frac_2.numerator):
            return True
        else:
            return False

    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True

    def __lt__(self, other):
        diff = self - other
        if (diff.numerator < 0) ^ (diff.denominator < 0):
            return True
        else:
            return False

    def __le__(self, other):
        diff = self - other
        if (diff.numerator <= 0) ^ (diff.denominator <= 0):
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

    def Simplify(self):
        a = GCD(self.numerator, self.denominator)
        return Fraction(int(self.numerator / a), int(self.denominator / a))


class FractionTest(unittest.TestCase):
    '''
    def test_init(self):
        """Initiate fraction in test"""
        case = Fraction(1, 2)
        self.assertEqual(case.numerator, 1)
        self.assertEqual(case.denominator, 2)

    def test_raise(self):
        """Test except in Fraction"""
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

    def test_add(self):
        """Test addition in Fraction"""
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        case_3 = Fraction(1, 4)
        self.assertEqual((case_1 + case_2), Fraction(5, 6))
        self.assertEqual(case_1 + case_2 + case_3, Fraction(13, 12))

    def test_sub(self):
        """Test subtraction in Fraction"""
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        self.assertEqual((case_1 - case_2), Fraction(1, 6))

    def test_mul(self):
        """Test multiple in Fraction"""
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        self.assertEqual(case_1 * case_2, Fraction(1, 6))

    def test_divide(self):
        """Test division in Fraction"""
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        self.assertEqual(case_1 / case_2, Fraction(3, 2))

    def test_ne(self):
        """Test NotEqual in Fration"""
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        self.assertEqual(case_1 != case_1, False)
        self.assertEqual(case_1 != case_2, True)

    def test_lt(self):
        """Teest less than in Fraction"""
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        case_3 = Fraction(1, -2)
        case_4 = Fraction(-1, 3)
        case_5 = Fraction(-1, 2)
        case_6 = Fraction(1, -3)
        self.assertEqual(case_3 < case_4, True)
        self.assertEqual(case_5 < case_6, True)
        self.assertEqual(case_1 < case_2, False)
        self.assertEqual(case_2 < case_1, True)

    def test_le(self):
        """Test less than or equal to in Fraction"""
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        case_3 = Fraction(1, -2)
        case_4 = Fraction(-1, 3)
        case_5 = Fraction(-1, 2)
        case_6 = Fraction(1, -3)
        self.assertEqual(case_3 <= case_4, True)
        self.assertEqual(case_5 <= case_6, True)
        self.assertEqual(case_1 <= case_1, True)
        self.assertEqual(case_1 <= case_2, False)
        self.assertEqual(case_2 <= case_1, True)

    def test_gt(self):
        """Test greater than in Fraction"""
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        case_3 = Fraction(1, -2)
        case_4 = Fraction(-1, 3)
        case_5 = Fraction(-1, 2)
        case_6 = Fraction(1, -3)
        self.assertEqual(case_3 > case_4, False)
        self.assertEqual(case_5 > case_6, False)
        self.assertEqual(case_1 > case_2, True)
        self.assertEqual(case_2 > case_2, False)

    def test_ge(self):
        """Test greater than or equal to in Fration"""
        case_1 = Fraction(1, 2)
        case_2 = Fraction(1, 3)
        case_3 = Fraction(1, -2)
        case_4 = Fraction(-1, 3)
        case_5 = Fraction(-1, 2)
        case_6 = Fraction(1, -3)
        self.assertEqual(case_3 >= case_4, False)
        self.assertEqual(case_5 >= case_6, False)
        self.assertEqual(case_1 >= case_1, True)
        self.assertEqual(case_1 >= case_2, True)
        self.assertEqual(case_2 >= case_1, False)
    '''

    def test_simplify(self):
        ''' Test of Simplify() '''
        case_1 = Fraction(1, 2)
        case_2 = Fraction(2, 4)
        case_3 = Fraction(-1, 3)
        case_4 = Fraction(3, -9)
        self.assertEqual(case_1, case_2)
        self.assertEqual(case_1, case_2.Simplify())
        self.assertEqual(case_3, case_4)


def getInput():
    """Literally get inputs"""
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
    # Initialization of Q
    while Q != 'Q' and Q != 'q':
        print(UserDoing())
        Q = input('Input any characters except Q/q to continue: ')

    print('Main function ended. \n')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    """
        exit=False means do not invoke exit() after error/fail
        verbosity=2 means input detailed msg
    """
    '''
    main()
    '''
