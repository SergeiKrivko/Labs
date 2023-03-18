from math import inf
import math

ERRORS_INFO = {'0': 'Корень найден успешно',
               '1': 'Перевышение максимального количества итераций',
               '2': 'Деление на ноль',
               '3': 'Другая ошибка при вычислении значения функции',
               '4': '',
               '5': ''}


def binary_search_method(function, a, b, eps, max_iter_count=inf):
    if function(a) * function(b) > 0:
        return None, None, None, 0
    x = (a + b) / 2
    iter_count = 0
    while abs(function(x)) >= eps and iter_count < max_iter_count:
        iter_count += 1
        if function(a) * function(x) > 0:
            a = x
        else:
            b = x
        x = (a + b) / 2
    return x, function(x), iter_count, None


def simple_iteration_method(func, der, a, b, eps, max_iter):
    try:
        if func(a) * func(b) > 0:
            return None, None, 0, -1
        q = 1 / der(a)
        x = a
        f = func(x)
    except ZeroDivisionError:
        return None, None, 0, 2
    except Exception:
        return None, None, 0, 3

    iters = 0
    while True:
        iters += 1
        x = x - q * f
        if x < a or x > b:
            return None, None, iters, -1
        if iters >= max_iter:
            return None, None, iters, 1
        try:
            f = func(x)
        except ZeroDivisionError:
            return None, None, iters, 2
        except Exception:
            return None, None, iters, 3

        if abs(f) < eps or abs(q * f) < eps:
            return x, f, iters, 0


def find_roots(func, der, a, b, eps, h, max_iter):
    x = a
    while x + h < b + h / 2:
        yield (x, x + h), simple_iteration_method(func, der, x, x + h, eps, max_iter)
        x += h


def main():
    def f(x):
        return math.sin(x)

    def der(x):
        return math.cos(x)

    for el in find_roots(f, der, -10, 10, 1e-12, 1, 1000):
        print(el)


if __name__ == '__main__':
    main()
