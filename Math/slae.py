from matrix import Matrix
import in_out


class Polynom:
    def __init__(self, array):
        self.array = array
        self.len = len(array)

    def __mul__(self, other):
        a = []
        for i in range(self.len):
            a.append(self.array[i] * other)
        return Polynom(a)

    def __rmul__(self, other):
        a = []
        for i in range(self.len):
            a.append(self.array[i] * other)
        return Polynom(a)

    def __add__(self, other):
        if self.len != other.len:
            return ValueError('Polynoms have different sizes')
        new = []
        for i in range(self.len):
            new.append(self.array[i] + other.array[i])
        return Polynom(new)

    def __str__(self):
        return str(self.array)

    def __format__(self, format_spec):
        return '{0:{1}}'.format(str(self), format_spec)

    def mul(self, other):
        a = []
        for i in range(self.len):
            a.append(self.array[i] * other)
        return Polynom(a)


def mul_polynom_matrix(self, other):
    if other.__class__.__name__ != 'Matrix':
        a = []
        for i in range(self.size_n):
            a.append([])
            for j in range(self.size_m):
                a[i].append(self.mtrx[i][j] * other)
        return Matrix(a)
    if self.size_m != other.size_n:
        raise ValueError('Matrices have different sizes')
    c = Matrix([[0] * other.size_m for i in range(self.size_n)])
    for i in range(self.size_n):
        for j in range(other.size_m):
            s = Polynom([0] * other.mtrx[0][0].len)
            for k in range(other.size_n):
                s += other.mtrx[k][j] * self.mtrx[i][k]
            c.mtrx[i][j] = s
    return c


def solve_slae(matrix_a, matrix_b=None):
    """Решение системы линейных алгебраических уравнений"""
    if matrix_b is None and isinstance(matrix_a, tuple):
        matrix_b = matrix_a[1]
        matrix_a = matrix_a[0]
    matrix = matrix_a.__copy__()
    for i in range(matrix.size_n):
        matrix.mtrx[i].append(matrix_b.mtrx[i][0])
    if matrix.rang() != (r := matrix_a.rang()):
        return 'Решений нет'
    if r < matrix_a.size_m:
        basic_variables = []
        free_variables = list(range(matrix_a.size_m))
        e = []
        a = matrix_a.__copy__()
        if not a.is_square():
            a.make_square()
        a = a.mtrx
        order = list(range(len(a)))
        for i in range(len(a)):
            for j in range(i):
                if a[i][j] != 0:
                    if abs(a[j][j]) > 1e-12:
                        c = a[i][j] / a[j][j]
                        a[i][j] = 0
                        for k in range(j + 1, len(a)):
                            a[i][k] -= c * a[j][k]
                    else:
                        a[i], a[j] = a[j], a[i]
                        order[i], order[j] = order[j], order[i]
        for i in range(len(a)):
            if abs(a[i][i]) > 1e-10:
                free_variables.remove(i)
                basic_variables.append(i)
                e.append(order[i])
        matrix_of_polynoms = []
        basic_minor = []
        for i in range(len(e)):
            pol = [0] * (len(a) + 1)
            pol[0] = matrix_b.mtrx[i][0]
            for j in range(len(free_variables)):
                pol[free_variables[j] + 1] = -matrix_a.mtrx[e[i]][free_variables[j]]
            matrix_of_polynoms.append(Polynom(pol))
            basic_minor.append([])
            for j in range(len(basic_variables)):
                basic_minor[i].append(matrix_a.mtrx[e[i]][basic_variables[j]])
        basic_minor = Matrix(basic_minor)
        matrix_of_polynoms = Matrix([matrix_of_polynoms])
        matrix_of_polynoms.transpose()
        return basic_variables, mul_polynom_matrix(basic_minor ** -1, matrix_of_polynoms)
    return matrix_a ** -1 * matrix_b


def input_slae(function=int, print_slae=False):
    matrix_a = []
    matrix_b = []
    size_n = in_out.input_value('Введите кол-во уравнений')
    size_m = in_out.input_value('Введите кол-во переменных')
    for i in range(size_n):
        print('Уравнение {}:'.format(i + 1))
        matrix_a.append([])
        for j in range(size_m):
            matrix_a[i].append(in_out.input_value('Введите коэффициент при x{}'.format(j + 1), function))
        matrix_b.append([in_out.input_value('Введите свободный член', function)])
    if print_slae:
        print()
        for i in range(size_n):
            print('{}*x{}'.format(matrix_a[i][0], 1), end='')
            for j in range(1, size_m):
                if matrix_a[i][j] > 0:
                    print(' + {}*x{}'.format(matrix_a[i][j], j + 1), end='')
                elif matrix_a[i][j] < 0:
                    print(' - {}*x{}'.format(-matrix_a[i][j], j + 1), end='')
            print(' = {}'.format(matrix_b[i][0]))
        print()
    return Matrix(matrix_a), Matrix(matrix_b)


def print_slae_solve(solve):
    if isinstance(solve, tuple):
        basic_variables = solve[0]
        solve = solve[1].mtrx
        for i in range(len(basic_variables)):
            print('x{0} = '.format(basic_variables[i] + 1), end='')
            if solve[i][0].array[0] != 0:
                print('{0}'.format(solve[i][0].array[0]), end='')
            for j in range(1, len(solve[0][0].array)):
                if j - 1 not in basic_variables:
                    if solve[i][0].array[j] > 0:
                        print(' + {}*x{}'.format(solve[i][0].array[j], j), end='')
                    elif solve[i][0].array[j] < 0:
                        print(' - {}*x{}'.format(-solve[i][0].array[j], j), end='')
            print()
    else:
        print(solve)
