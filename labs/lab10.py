#   Кривко Сергей ИУ7-14Б
# Вычисление приближённого значения интеграла
# известной, заданной в программе, функции методами левых прямоугольников и 3/8

import math
import in_out


def f(x):
    return 2 * x


def F(x):
    """Первообразная функции f(x)"""
    return x ** 2


def integral_left(start, stop, count):
    """Вычисление интеграла методом левых прямоугольников"""
    current_value = start
    step = (stop - start) / count
    integral_value = 0
    try:
        while current_value <= stop + step / 2:
            integral_value += f(current_value) * step
            current_value += step
    except Exception:
        return None
    return integral_value


def integral_38(start, stop, count):
    """Вычисление интеграла методом 3/8"""
    current_value = start
    if count % 3 == 1:
        count += 2
    elif count % 3 == 2:
        count += 1
    step = (stop - start) / count
    integral_value = 0
    try:
        while current_value <= stop + step / 2:
            integral_value += (f(current_value) + 3 * f(current_value + step) + 3 * f(current_value + 2 * step)
                               + f(current_value + 3 * step))
            current_value += 3 * step
    except Exception:
        return None
    return integral_value * 3 / 8 * step


def absolute_error(value):
    """Абсолютная погрешность вычисления интеграла"""
    return abs(integral - value)


def relative_error(value):
    """Относительная погрешность вычисления интеграла"""
    if integral == 0:
        return float('inf')
    return absolute_error(value) / abs(integral)


def accuracy(function, value, epsilon):
    """Вычисление количества итераций, необходимых для заданной точности"""
    while abs(function(value) - function(2 * value)) >= epsilon:
        value *= 2
    return value




# Ввод значений
start_value = in_out.input_value('Введите начало отрезка', float)
while True:
    stop_value = in_out.input_value('Введите конец отрезка', float)
    if stop_value > start_value:
        break
    print('Введите число, превышающее начало отрезка')
count1 = in_out.input_value('Введите первое кол-во участков разбиения', int, only_positive=True)
count2 = in_out.input_value('Введите второе кол-во участков разбиения', int, only_positive=True)


# Значение интеграла, вычисленное методом левых прямоугольников для count1 участков разбиения
integral_left_1 = integral_left(start_value, stop_value, count1)
# Значение интеграла, вычисленное методом левых прямоугольников для count2 участков разбиения
integral_left_2 = integral_left(start_value, stop_value, count2)

# Значение интеграла, вычисленное методом 3/8 для count1 участков разбиения
integral_38_1 = integral_38(start_value, stop_value, count1)
# Значение интеграла, вычисленное методом 3/8 для count2 участков разбиения
integral_38_2 = integral_38(start_value, stop_value, count2)

if integral_38_1 is None or integral_38_2 is None or integral_left_1 is None or integral_left_2 is None:
    print('Не удалось вычислить интеграл. Вероятно, функция определена не на всем отрезке')
else:
    print('\nЗначения интеграла:')
    in_out.print_table_from_rows(['Метод', '{0} участков'.format(count1), '{0} участков'.format(count2)],
                                 ['Левых прямоугольников', integral_left_1, integral_left_2],
                                 ['3/8', integral_38_1, integral_38_2],
                                 row_sep='')

    try:
        integral = F(stop_value) - F(start_value)  # Точное значение интеграла
    except Exception:
        print('\nНе удалось вычислить точное значение интеграла')
    else:
        print('\nТочное значение интеграла {:<7g}'.format(integral))

        print('\nАбсолютные погрешности:')
        in_out.print_table_from_rows(['Метод', '{0} участков'.format(count1), '{0} участков'.format(count2)],
                                     ['Левых прямоугольников', absolute_error(integral_left_1),
                                      absolute_error(integral_left_2)],
                                     ['3/8', absolute_error(integral_38_1), absolute_error(integral_38_2)],
                                     row_sep='')

        print('\nОтносительные погрешности:')
        in_out.print_table_from_rows(['Метод', '{0} участков'.format(count1), '{0} участков'.format(count2)],
                                     ['Левых прямоугольников', relative_error(integral_left_1),
                                      relative_error(integral_left_2)],
                                     ['3/8', relative_error(integral_38_1), relative_error(integral_38_2)],
                                     row_sep='')

        # Определение более точного метода
        if min(relative_error(integral_left_1), relative_error(integral_left_2)) < \
                min(relative_error(integral_38_1), relative_error(integral_38_2)):
            print('\nМетод левых прямоугольников более точный')
            less_accuracy_method = lambda cnt: integral_38(start_value, stop_value, cnt)
        else:
            print('\nМетод 3/8 более точный')
            less_accuracy_method = lambda cnt: integral_left(start_value, stop_value, cnt)

        epsilon = in_out.input_value('Введите необходимую точность', float, only_positive=True)

        print('Для того, чтобы другой метод вычислил значение с заданной точностью, необходимо',
              accuracy(less_accuracy_method, min(count1, count2), epsilon), 'участков разбиения')
