from math import gcd


class Fraction:
    def __init__(self, numerator, denominator=1, checking=False):
        if isinstance(numerator, str) and '/' in numerator:
            a = numerator.split('/')
            self.numerator = int(a[0])
            self.denominator = int(a[1])
        else:
            self.numerator = int(numerator)
            self.denominator = int(denominator)
        self.simplify()

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        return float(self) == float(other)

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return (self * other.denominator).numerator.__ge__((other * self.denominator).numerator)
        return float(self).__ge__(float(other))

    def __le__(self, other):
        if isinstance(other, Fraction):
            return (self * other.denominator).numerator.__le__((other * self.denominator).numerator)
        return float(self).__le__(float(other))

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return (self * other.denominator).numerator.__gt__((other * self.denominator).numerator)
        return float(self).__gt__(float(other))

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return (self * other.denominator).numerator.__lt__((other * self.denominator).numerator)
        return float(self).__lt__(float(other))

    def __neg__(self):
        return self * (-1)

    def __str__(self):
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1
        if self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator) + '/' + str(self.denominator)

    def __abs__(self):
        return Fraction(abs(self.numerator), abs(self.denominator))

    def __float__(self):
        return self.numerator / self.denominator

    def __mul__(self, other):
        if isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator).simplify()
        if isinstance(other, float):
            return float(self) * other
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator).simplify()
        raise ValueError(f'unsupported operand type(s) for *: "Fraction" and "{other.__class__.__name__}"')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Fraction(self.numerator, self.denominator * other)
        if isinstance(other, float):
            return float(self) / other
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator).simplify()
        raise ValueError(f'unsupported operand type(s) for /: "Fraction" and "{other.__class__.__name__}"')

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __pow__(self, power, modulo=None):
        if isinstance(power, int):
            return Fraction(self.numerator ** power, self.denominator ** power)
        return float(self).__pow__(power, modulo)

    def __add__(self, other):
        if isinstance(other, int):
            return Fraction(self.numerator + other * self.denominator, self.denominator).simplify()
        if isinstance(other, float):
            return float(self) + other
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator
                            * other.denominator).simplify()
        raise ValueError(f'unsupported operand type(s) for +: "Fraction" and "{other.__class__.__name__}"')

    def __sub__(self, other):
        if isinstance(other, int):
            return Fraction(self.numerator - other * self.denominator, self.denominator).simplify()
        if isinstance(other, float):
            return float(self) - other
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator
                            * other.denominator).simplify()
        raise ValueError(f'unsupported operand type(s) for -: "Fraction" and "{other.__class__.__name__}"')

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __format__(self, format_spec):
        return '{0:{1}}'.format(self.__str__(), format_spec)

    def simplify(self):
        x = gcd(self.numerator, self.denominator)
        self.numerator //= x
        self.denominator //= x
        return self
