# Coded by ZiyuZhang
# Fraction calculator
# I was trying to simplify fractions, but I falled concerning about domain of definition
# but I left them as annotations for studying in future


class Fraction:
    """
        This class represents a object of fractions including its calculations.
        There are 5 member fuctions(methods):
        'plus()': simply add 2 fractions together
        'minus()': let the first one be reduced by the second one
        'times()': multiply 2 fractions
        'divide()': 1 fraction divided by another
        'equal()': if 1 fraction equals another, return true, else return false
        2 members(attributes):
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
            raise ZeroDivisionError('Denominator cannot be zero. \n')

    def plus(self, other):
        # Num = self.numerator * other.denominator / GCD(self.denominator, other.denominator) + other.numerator * self.denominator / GCD(self.denominator, other.denominator)
        # Den = LCM(self.denominator, other.denominator)
        Num = self.numerator * other.denominator + other.numerator * self.denominator
        Den = self.denominator * other.denominator
        return Fraction(Num, Den)

    def minus(self, other):
        # Num = self.numerator * other.denominator / GCD(self.denominator, other.denominator) - other.numerator * self.denominator / GCD(self.denominator, other.denominator)
        # Den = LCM(self.denominator, other.denominator)
        Num = self.numerator * other.denominator - other.numerator * self.denominator
        Den = self.denominator * other.denominator
        return Fraction(Num, Den)

    def times(self, other):
        Num = self.numerator * other.numerator
        Den = self.denominator * other.denominator
        # i = GCD(Num, Den)
        # return Fraction(Num / i, Den / i)
        return (Num, Den)

    def divide(self, other):
        Num = self.numerator * other.denominator
        Den = self.denominator * other.numerator
        # i = (Num, Den)
        return Fraction(Num, Den)

    def equal(self, other):
        '''
        if Simplify(self) == Simplify(other):
            return True
        else:
            return False
        '''
        if (self.numerator * other.denominator) == (other.numerator * self.denominator):
            return True
        else:
            return False

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


def FracSum(Frac1, Frac2):
    """
        I do not want to rewrite print(frac1.plus(frac2)) or something else again and again
        so I define these 5 functions
        Their function can be easily identified by names
    """
    Sum = Frac1.plus(Frac2)
    return (Frac1.__str__() + ' + ' + Frac2.__str__() + ' = ' + Sum.__str__() + '\n')


def FracDiff(Frac1, Frac2):
    Diff = Frac1.minus(Frac2)
    return (Frac1.__str__() + ' - ' + Frac2.__str__() + ' = ' + Diff.__str__() + '\n')


def FracProduct(Frac1, Frac2):
    Product = Frac1.times(Frac2)
    return (Frac1.__str__() + ' * ' + Frac2.__str__() + ' = ' + Product.__str__() + '\n')


def FracQuotient(Frac1, Frac2):
    Quotient = Frac1.divide(Frac2)
    return ('( ' + Frac1.__str__() + ' )' + ' / ' + '( ' + Frac2.__str__() + ' ) = ' + Quotient.__str__() + '\n')


def IsEqual(Frac1, Frac2):
    if Frac1.equal(Frac2):
        return (Frac1.__str__() + '==' + Frac2.__str__() + '\n')
    else:
        return (Frac1.__str__() + '!=' + Frac2.__str__() + '\n')


def test():
    """
        this part is just for testing whether calss can work well.
    """
    frac_1 = Fraction(1, 2)
    frac_2 = Fraction(1, 3)
    frac_3 = Fraction(3, 4)

    print('Test begin. \n')
    print('Fraction 1: ', frac_1, '\n')
    print('Fraction 2: ', frac_2, '\n')
    print('Fraction 3: ', frac_3, '\n')

    print(FracSum(frac_1, frac_2))
    print(FracDiff(frac_1, frac_2))
    print(FracProduct(frac_1, frac_2))
    print(FracQuotient(frac_1, frac_2))
    print(IsEqual(frac_1, frac_2))
    print(frac_1, ' + ', frac_2, ' + ', frac_3, ' = ', frac_1.plus(frac_2.plus(frac_3)))

    print('Test end. \n')


def UserDoing():
    """
        Modifying is always good
    """
    print('Input 2 fractions')

    Num_1 = input('Input fraction 1 numerator: ')
    Den_1 = input('Input fraction 1 denominator: ')
    Operator = input('Input operator(+, -, *, /, =): ')
    Num_2 = input('Input fraction 2 numerator: ')
    Den_2 = input('Input fraction 2 denominator: ')

    Frac1 = Fraction(float(Num_1), float(Den_1))
    Frac2 = Fraction(float(Num_2), float(Den_2))

    if Operator == '++':
        return Frac1.plus(Frac1)

    OpDic = {'+': FracSum(Frac1, Frac2), '-': FracDiff(Frac1, Frac2), '*': FracProduct(Frac1, Frac2), '/': FracQuotient(Frac1, Frac2), '=': IsEqual(Frac1, Frac2)}
    return OpDic[str(Operator)]


def main():
    """
        main function. In this section. We will invoke test()
        and we will let users to do some operations of fractions with UserDoing()
    """
    test()
    print('Main function started. \n')
    Q = 'Easter Egg is in line 152'

    while Q != 'Q' and Q != 'q':
        print(UserDoing())
        Q = input('Input any characters except Q/q to continue: ')

    print('Main function ended. \n')


if __name__ == '__main__':
    main()
