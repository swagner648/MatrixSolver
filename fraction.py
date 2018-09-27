
class Fraction:
    def __init__(self, top, bottom):
        if bottom == 0 and top != 0:
            raise ZeroDivisionError("Fraction cannot have a zero denominator and non-zero numerator")

        if top == 0:
            bottom = 0

        if top < 0 and bottom < 0:
            top = -top
            bottom = -bottom

        if top >= 0 and bottom < 0:
            top = -top
            bottom = -bottom

        self.num = top
        self.den = bottom

        for i in reversed(range(1, abs(self.num) + 1)):
            if self.den % i == 0 and self.num % i == 0:
                self.num = int(self.num / i)
                self.den = int(self.den / i)

    def __add__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        if self.den == 0:
            return other
        if other.den == 0:
            return self
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __radd__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        if self.den == 0:
            return other
        if other.den == 0:
            return self
        num = other.num * self.den + self.num * other.den
        den = other.den * self.den
        return Fraction(num, den)

    def __sub__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        if self.den == 0:
            return other
        if other.den == 0:
            return self
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __rsub__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        if self.den == 0:
            return other
        if other.den == 0:
            return self
        num = other.num * self.den - self.num * other.den
        den = other.den * self.den
        return Fraction(num, den)

    def __mul__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __rmul__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def __rtruediv__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        num = other.num * self.den
        den = other.den * self.num
        return Fraction(num, den)

    def __mod__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        temp = Fraction(self.num, self.den)
        while other < temp:
            temp = temp - other
        return temp

    def __rmod__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        temp = Fraction(self.num, self.den)
        while other < temp:
            temp = temp - other
        return temp

    def __repr__(self):
        if self.den == 1 or self.num == 0:
            string = str(self.num)
        else:
            string = str(self.num) + "/" + str(self.den)
        return string

    def __eq__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        if self.num == 0 and other.num == 0:
            return True
        return self.num == other.num and self.den == other.den

    def __ne__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        if self.num == 0 and other.num == 0:
            return False
        return self.num != other.num or self.den != other.den

    def __lt__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        num1 = self.num * other.den
        num2 = other.num * self.den
        return num1 < num2

    def __gt__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        num1 = self.num * other.den
        num2 = other.num * self.den
        return num1 > num2

    def __le__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        num1 = self.num * other.den
        num2 = other.num * self.den
        return num1 <= num2

    def __ge__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        num1 = self.num * other.den
        num2 = other.num * self.den
        return num1 >= num2

    def __neg__(self):
        return Fraction(-self.num, self.den)
