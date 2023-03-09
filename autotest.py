import in_out
from speed_test import timeit
import random


def autotest(func1, func2, generate_random_value, equal=None, test_count=100):
    if test_count <= 0:
        test_count = in_out.input_value('Введите кол-во тестов', int, only_positive=True)
    count = 0
    for i in range(test_count):
        a = generate_random_value()
        b = func1(a)
        c = func2(a)
        if equal and equal(b, c) or b == c:
            pass
            # print('Тест №{0}: результат верный'.format(i + 1))
        else:
            print(f'Тест №{i + 1}: \nИсходные данные: {a}\nОжидаемый ответ: {b}\nПолученный ответ: {c}')
            count += 1
    print('------------------------------------------------')
    print(f'Тестирование завершено. Неверных тестов: {count} из {test_count}')


def generate_random_matrix(size=3):
    return [[random.randint(-size, size) for j in range(size)] for i in range(size)]


def generate_random_array(size=3):
    return [random.randint(-size, size) for i in range(size)]
