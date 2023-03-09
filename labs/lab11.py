#   Кривко Сергей ИУ7-14Б
# Сортировка массива методом вставок с барьером

import in_out
import time
import random


def barrier_insertion_method(array):
    t = time.time()
    count = 0
    n = len(array)
    a = [0] + array
    for i in range(2, n + 1):
        if a[i - 1] > a[i]:
            a[0] = a[i]
            j = i - 1
            while a[j] > a[0]:
                a[j + 1] = a[j]
                j -= 1
                count += 1
            a[j + 1] = a[0]
    a.pop(0)
    t = time.time() - t
    return a, t, count

def heap_sort_method(array):
    t = time.time()
    n = len(array)
    a = array.copy()

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    for i in range(n, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)
    t = time.time() - t
    return a, t, 0

def heapify(arr, n, count_of_permutations):
    """
    Функция преобразования массива в двоичную кучу
    :param arr: Массив для преобразования
    :param n: Размер массива
    :param count_of_permutations: Количество перестановок
    :return: Изменяет исходный массив
    """
    for i in range(n - 1, -1, -1):
        j = (i - (2 if i % 2 == 0 else 1)) // 2
        if j >= 0 and arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
            count_of_permutations += 1


def heap_sort(arr, n):
    t = time.time()
    """
    Функция пирамидальной сортировки
    :param arr: Массив для сортировки
    :param n: Размер массива
    :return: Изменяет исходный массив, возращает количество перестановок
    """

    # Если родительский узел хранится в индексе I,
    # левый дочерний элемент может быть вычислен как 2 I + 1,
    # а правый дочерний элемент — как 2 I + 2

    # Количество перестановок
    count_of_permutations = 0
    while n > 0:
        # Преобразование массива в двоичную кучу
        heapify(arr, n, count_of_permutations)
        if arr[0] != arr[n - 1]:
            # Перестановка первого и последнего элементов
            arr[0], arr[n - 1] = arr[n - 1], arr[0]
            count_of_permutations += 1
        # Уменьшение размера кучи
        n -= 1
        t = time.time() - t
    return count_of_permutations, t

def generate_random_array(size):
    return [random.randint(-size, size) for i in range(size)]


a = in_out.input_array(int, name='A')

sorted_a = barrier_insertion_method(a)[0]

in_out.print_array_in_row(sorted_a, widht=8, name='Отсортированный массив A:')


print()
n1 = in_out.input_value('Введите первую размерность', only_positive=True)
n2 = in_out.input_value('Введите вторую размерность', only_positive=True)
n3 = in_out.input_value('Введите третью размерность', only_positive=True)


sorted_array = [list(range(n1)), list(range(n2)), list(range(n3))]
random_array = [generate_random_array(n1), generate_random_array(n2), generate_random_array(n3)]
reversed_array = [list(range(n1, 0, -1)), list(range(n2, 0, -1)), list(range(n3, 0, -1))]


times = [[0] * 3 for i in range(3)]
counts = [[0] * 3 for j in range(3)]
nnnn = [n1, n2, n3]
for i in range(3):
        b = heap_sort(sorted_array[i], nnnn[i])
        times[i][0] = b[1]
        counts[i][0] = b[0]
        b = heap_sort(random_array[i], nnnn[i])
        times[i][1] = b[1]
        counts[i][1] = b[0]
        b = heap_sort(reversed_array[i], nnnn[i])
        times[i][2] = b[1]
        counts[i][2] = b[0]

print()
in_out.print_table_from_rows(['размерность массива', n1, n2, n3],
                            ['', ['время, с', 'перестановки'], ['время, с', 'перестановки'], ['время, с', 'перестановки']],
                            ['упорядоченный список', [times[0][0], counts[0][0]], [times[1][0], counts[1][0]],
                                [times[2][0], counts[2][0]]],
                            ['случайный список', [times[0][1], counts[0][1]], [times[1][1], counts[1][1]],
                                [times[2][1], counts[2][1]]],
                            ['упорядоченный в обратном порядке список', [times[0][2], counts[0][2]], [times[1][2], counts[1][2]],
                                [times[2][2], counts[2][2]]])
