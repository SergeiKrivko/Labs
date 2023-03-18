"""
Модуль, содержащий функции для ввода и вывода различных данных
"""


class NegativeValueError(Exception):
    pass


def input_value(prompt='', function=int, only_positive=False, input_func=input):
    """
    Ввод числового значения
    :param prompt: приглашение к вводу
    :param function: функция для преобразования строки
    :param only_positive: проверка на неотрицательность
    :param input_func: функция для ввода (в случае ввода не из консоли)
    :return: None
    """
    while True:
        try:
            value = function(input_func(prompt + ': '))
            if only_positive and value <= 0:
                raise NegativeValueError
            return value
        except ValueError:
            if function == int:
                print('Введите целое число')
            else:
                print('Введите число')
        except NegativeValueError:
            print('Введите положительное число')
        except Exception:
            print('Неизвестная ошибка. Повторите ввод')


def input_array(function=int, size=0, name='\b'):
    """
    Ввод массива
    :param function: функция для преобразования к числам
    :param size: размер массива. По умолчанию вводится с клавиатуры
    :param name: имя массива
    :return: None
    """
    if size == 0:
        size = input_value('Введите длину массива {0}'.format((name)), int, only_positive=True)
    array = [0] * size
    for i in range(size):
        array[i] = input_value('Введите {0}-й элемент массива {1}'.format(i + 1, name), function)
    return array


def input_matrix(function=int, height=0, widht=0, square=False, name='\b', input_func=input):
    """
    Ввод матрицы
    :param function: функция для преобразования к числам
    :param height: кол-во строк в матрице (по умолчанию вводится с клваиатуры)
    :param widht: кол-во столбцов в матрице (по умолчанию вводится с клваиатуры)
    :param square: квадратная матрица
    :param name: имя матрицы
    :param input_func: функция для ввода (в случае ввода не из консоли)
    :return: None
    """
    if square:
        if height == 0:
            height = input_value('Введите размер квадратной матрицы {0}'.format(name), int, only_positive=True,
                                 input_func=input_func)
        widht = height
    else:
        if height == 0:
            height = input_value('Введите кол-во строк матрицы {0}'.format((name)), int, only_positive=True,
                                 input_func=input_func)
        if widht == 0:
            widht = input_value('Введите кол-во столбцов матрицы {0}'.format(name), int, only_positive=True,
                                input_func=input_func)
    matrix = [[0] * widht for i in range(height)]
    for i in range(height):
        for j in range(widht):
            matrix[i][j] = input_value('Введите элемент [{0}][{1}] матрицы {2}'.format(i + 1, j + 1, name), function,
                                       input_func=input_func)
    return matrix


def print_matrix(matrix, widht=0, name='Матрица'):
    '''Вывод матрицы'''
    if widht <= 0:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                try:
                    widht = max(widht, len('{:6g}'.format(matrix[i][j])))
                except Exception:
                    widht = max(widht, len(matrix[i][j]))
    print(name) if name != '' else print()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            try:
                print('{0:<{1}.6g}'.format(matrix[i][j], widht), end='  ')
            except Exception:
                print('{0:<{1}}'.format(matrix[i][j], widht), end='  ')
        print()


def print_array_in_row(array, widht=0, name=''):
    '''Вывод массива в строку'''
    if name is not None:
        print(name)
    if widht > 0:
        for i in range(len(array)):
            try:
                print('{:6g}'.format(array[i]), end=' ')
            except Exception:
                print(array[i], end=' ')
        print()
    else:
        for i in range(len(array)):
            try:
                print('{:5g}'.format(array[i]), end=', ')
            except Exception:
                print(array[i], end=', ')
        print('\b\b')


def print_array_in_column(array, name=''):
    '''Вывод массива в столбец'''
    print()
    if name != '':
        for i in range(len(array)):
            try:
                print('{0}[{1}] = {2:<7.6g}'.format(name, i + 1, array[i]))
            except Exception:
                print('{0}[{1}] = {2:<7}'.format(name, i + 1, array[i]))
    else:
        for i in range(len(array)):
            try:
                print('{:<7.6g}'.format(array[i]))
            except Exception:
                print('{:<7}'.format(array[i]))


def min_width(x, sep):
    if isinstance(x, list):
        width = len(sep) * (len(x) - 1)
        m = 0
        for el in x:
            m = max(m, min_width(el, sep))
        return width + m * len(x)
    else:
        try:
            return len('{:<6g}'.format(x))
        except Exception:
            return len(str(x))


def render(x, width, sep):
    if isinstance(x, list):
        width2 = (width - len(sep) * (len(x) - 1)) % len(x)
        width = (width - len(sep) * (len(x) - 1)) // len(x)
        s = ''
        for i in range(len(x)):
            s += render(x[i], width, sep)
            if i < width2:
                s += ' '
            if i != len(x) - 1:
                s += sep
        return s
    else:
        try:
            return '{0:<{1}.6g}'.format(x, width)
        except Exception:
            return '{0:<{1}}'.format(str(x), width)


def print_table_from_rows(*args, column_sep=' | ', row_sep='-', first_row_sep='-'):
    '''Печать данных в виде таблицы'''
    column_width = []
    table_width = len(args[0]) * len(column_sep)
    for j in range(len(args[0])):
        width = 0
        for i in range(len(args)):
            width = max(width, min_width(args[i][j], column_sep))
        column_width.append(width)
        table_width += width
    for i in range(len(args[0])):
        print(render(args[0][i], column_width[i], column_sep), column_sep, sep='', end='')
    print()
    if first_row_sep != '':
        print(first_row_sep * table_width)
    for i in range(1, len(args)):
        for j in range(len(args[0])):
            print(render(args[i][j], column_width[j], column_sep), column_sep, sep='', end='')
        print()
        if row_sep != '':
            print(row_sep * table_width)


def print_table_from_columns(*args, column_names=None, column_sep=' | ', row_sep='-', first_row_sep='-'):
    '''Печать данных в виде таблицы'''
    column_width = []
    table_width = len(args) * len(column_sep)
    for j in range(len(args)):
        width = 0
        if column_names is not None:
            width = max(width, min_width(column_names[j], column_sep))
        for i in range(len(args[0])):
            width = max(width, min_width(args[j][i], column_sep))
        column_width.append(width)
        table_width += width
    if column_names is not None:
        for i in range(len(column_names)):
            print(render(column_names[i], column_width[i], column_sep), column_sep, sep='', end='')
    print()
    if first_row_sep != '':
        print(first_row_sep * table_width)
    for i in range(len(args[0])):
        for j in range(len(args)):
            print(render(args[j][i], column_width[j], column_sep), column_sep, sep='', end='')
        print()
        if row_sep != '':
            print(row_sep * table_width)
