from fraction import Fraction


class Monomial:
    def __init__(self, coefficient, *variables, powers=None):
        def split_by_power(s):
            s = s.split('^')
            if len(s) == 2:
                return s[0], int(s[1])
            elif len(s) == 1:
                return s[0], 1
            raise ValueError

        if isinstance(coefficient, str) and len(variables) == 0:
            array = coefficient.split('*')
            try:
                coefficient = Fraction(array[0])
                variables = array[1:]
            except ValueError:
                coefficient = 1
                variables = array
            for i in range(len(variables)):
                variables[i] = split_by_power(variables[i])
        self.coefficient = coefficient
        if powers is not None:
            self.variables = list(variables)
            self.powers = powers
        else:
            self.variables = []
            self.powers = dict()
            for el in variables:
                if isinstance(el, tuple) and len(el) >= 1:
                    if el[0] in self.variables:
                        self.powers[el[0]] += el[1]
                    else:
                        self.variables.append(el[0])
                        self.powers[el[0]] = el[1]
                elif el in self.variables:
                    self.powers[el] += 1
                else:
                    self.variables.append(el)
                    self.powers[el] = 1
        self.variables.sort()

    def equal(self, other):
        return self.variables == other.variables and self.powers == other.powers

    def __mul__(self, other):
        if isinstance(other, Monomial):
            variables = []
            for i in range(len(self.variables)):
                variables.append((self.variables[i], self.powers[self.variables[i]]))
            for i in range(len(other.variables)):
                variables.append((other.variables[i], other.powers[other.variables[i]]))
            return Monomial(self.coefficient * other.coefficient, *variables)
        return Monomial(self.coefficient * other, *self.variables, powers=self.powers)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        s = [str(self.coefficient)]
        for el in self.variables:
            if self.powers[el] != 0:
                if self.powers[el] == 1:
                    s.append(el)
                else:
                    s.append(el + '^' + str(self.powers[el]))
        return '*'.join(s)

    def __neg__(self):
        return self * (-1)

    def __abs__(self):
        if self.coefficient < 0:
            return self * (-1)
        return self


class Polynom:
    def __init__(self, *args):
        def split_by_pluses_and_minuses(s):
            s = s.replace(' ', '')
            lst = []
            level = 0
            j = -1
            for i in range(len(s)):
                if s[i] == '+' and level == 0:
                    lst.append(s[j + 1:i])
                    j = i
                if s[i] == '-' and level == 0:
                    lst.append(s[j + 1:i])
                    j = i - 1
                elif s[i] == '(':
                    level += 1
                elif s[i] == ')':
                    level -= 1
            lst.append(s[j + 1:])
            return lst

        def split_by_star(s):
            lst = []
            level = 0
            j = -1
            for i in range(len(s)):
                if s[i] == '*' and level == 0:
                    lst.append(s[j + 1:i])
                    j = i
                elif s[i] == '(':
                    level += 1
                elif s[i] == ')':
                    level -= 1
            lst.append(s[j + 1:])
            return lst

        def create_polynom(s):
            lst = split_by_star(s)
            res = Polynom(Monomial(1))
            for el in lst:
                if '(' in el:
                    el = el.split('^')
                    if len(el) == 1:
                        el.append(1)
                    else:
                        el[1] = int(el[1])
                    res *= Polynom(el[0][1:-1]) ** el[1]
                else:
                    res *= Monomial(el)
            return res

        if isinstance(args[0], str):
            lst = split_by_pluses_and_minuses(args[0].replace('**', '^'))
            if '(' in lst[0]:
                pol = create_polynom(lst[0])
            else:
                pol = Polynom(Monomial(lst[0]))
            for i in range(1, len(lst)):
                if '(' in lst[i]:
                    pol += create_polynom(lst[i])
                else:
                    pol += Monomial(lst[i])
            self.array = pol.array
        else:
            self.array = list(args)
            self.simplify()

    def __mul__(self, other):
        if isinstance(other, Polynom):
            a = []
            for i in range(len(self.array)):
                for j in range(len(other.array)):
                    a.append(self.array[i] * other.array[j])
            return Polynom(*a)
        a = []
        for i in range(len(self.array)):
            a.append(self.array[i] * other)
        return Polynom(*a)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if not isinstance(other, Polynom):
            other = Polynom(other)
        a = self.array + other.array
        return Polynom(*a)

    def __radd__(self, other):
        return self.__add__(other)

    def __pow__(self, power, modulo=None):
        if power < 0:
            raise ValueError
        if power == 0:
            return 1
        a = self
        for i in range(1, power):
            a *= self
        return a

    def __str__(self):
        s = [str(self.array[0])]
        for i in range(1, len(self.array)):
            if self.array[i].coefficient > 0:
                s.append(' + ' + str(self.array[i]))
            elif self.array[i].coefficient < 0:
                s.append(' - ' + str(-self.array[i]))
        return ''.join(s)

    def simplify(self):
        i = 0
        while i < len(self.array):
            j = i + 1
            while j < len(self.array):
                if self.array[j].equal(self.array[i]):
                    self.array[i].coefficient += self.array[j].coefficient
                    self.array.pop(j)
                else:
                    j += 1
            i += 1
