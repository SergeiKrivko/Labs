import polynom
from matrix import Matrix
from fraction import Fraction
import slae
import angem
import linal


def remove_space(string):
    return string.replace(' ', '')


def input_matrix_of_int():
    return Matrix(name=var, function=int)


def input_matrix_of_float():
    return Matrix(name=var, function=float)


def input_matrix_of_fractions():
    return Matrix(name=var, function=Fraction)


def tr(matrix):
    return matrix.transpose()


def smart_input(s):
    for function in [angem.Plane.from_str, angem.Vector.from_str, angem.Point.from_str, Fraction]:
        try:
            return function(s)
        except Exception:
            pass
    return


def smart_input2(s):
    try:
        return Fraction(s)
    except Exception:
        return eval(s)


def command_slae():
    s = slae.input_slae(function=Fraction, print_slae=True)
    print('Решение:')
    slae.print_slae_solve(slae.solve_slae(s[0], s[1]))
    print()


variables = {'det': Matrix.determinant, 'opp': Matrix.opposite, 'tr': tr, 'rank': Matrix.rang, 'rg': Matrix.rang,
             'imatrix': input_matrix_of_int, 'fmatrix': input_matrix_of_float, 'frmatrix': input_matrix_of_fractions,
             'slae': command_slae, 'angem': angem, 'ag': angem, 'vector': linal.Vector, 'basis': linal.Basis,
             'polynom': polynom.Polynom, 'monomial': polynom.Monomial, 'circle': angem.Circle, 'sphere': angem.Sphere,
             'matrix': Matrix}


def execute_command(com):
    if com.strip() == '':
        return Matrix(name=var, function=smart_input2)
    a = smart_input(com)
    if a is not None:
        return a
    try:
        return eval(com, variables)
    except Exception as ex:
        print(f'{ex.__class__.__name__}: {ex}')


while True:
    command = input('>>> ')
    if command == 'exit':
        break
    elif '=' in command:
        i = command.index('=')
        var, arg = command[:i - 1].strip(), command[i + 1:].strip()
        for symbol in '-+*/ ().,':
            if symbol in var:
                arg = command.strip()
                res = execute_command(arg)
                if res:
                    print(res)
                break
        variables[var] = execute_command(arg)
    else:
        arg = command.strip()
        res = execute_command(arg)
        if res:
            print(res)
