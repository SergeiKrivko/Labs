import random
import in_out
import math


def compare_arrays(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True


def barrier_insertion_method(array):
    n = len(array)
    a = [0] + array
    for i in range(2, n + 1):
        if a[i - 1] > a[i]:
            a[0] = a[i]
            j = i - 1
            while a[j] > a[0]:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = a[0]
    a.pop(0)
    return a


def insertion_method(array):
    n = len(array)
    a = array.copy()
    for i in range(1, n):
        if a[i - 1] > a[i]:
            x = a[i]
            j = i - 1
            while j >= 0 and x < a[j]:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = x
    return a


def binary_search_insertion_method(array):
    n = len(array)
    a = [array[0]]
    for i in range(1, n):
        left = 0
        right = i
        if array[i] > a[0]:
            while left < right:
                center = (left + right) // 2
                if a[center] < array[i]:
                    left = center + 1
                else:
                    right = center
        a.append(None)
        for j in range(i, left, -1):
            a[j] = a[j - 1]
        a[left] = array[i]
    return a


def shaker_method(array):
    n = len(array)
    a = array.copy()
    flag = True
    start_index = 0
    end_index = n - 1
    while flag:
        flag = False
        for i in range(start_index, end_index):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                flag = True
        if not flag:
            return a
        end_index -= 1
        for i in range(end_index, start_index, -1):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
                flag = True
        start_index += 1


def heap_sort_method(array):
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
    return a


def selection_method(array):
    n = len(array)
    a = array.copy()
    for i in range(n - 1):
        minimum = i
        for j in range(i + 1, n):
            if a[j] < a[minimum]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]
    return a


def shell_method(array):
    n = len(array)
    a = array.copy()
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = a[i]
            j = i
            while j >= interval and a[j - interval] > temp:
                a[j] = a[j - interval]
                j -= interval
            a[j] = temp
        k -= 1
        interval = 2**k - 1
    return a


def quick_sort(array):
    def partition(left, right):
        pivot = a[right]
        m = left
        for i in range(left, right):
            if a[i] <= pivot:
                a[i], a[m] = a[m], a[i]
                m += 1
        a[right], a[m] = a[m], a[right]
        return m

    def qsort(left, right):
        if left >= right:
            return
        m = partition(left, right)
        qsort(left, m - 1)
        qsort(m + 1, right)

    a = array.copy()
    qsort(0, len(a) - 1)
    return a


def bubble_sort(array):
    n = len(array)
    a = array.copy()
    flag = True
    while flag:
        flag = False
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                flag = True
    return a


def autotest(function):
    count = 0
    for i in range(10):
        length = random.randint(1, 100000)
        arr = [random.randint(-length, length) for i in range(length)]
        sorted_array = arr.copy()
        sorted_array.sort()
        sorted_by_method_array = function(arr)
        if sorted_array == sorted_by_method_array:
            print('Тест {0}: длина = {1}. Результат верный'.format(i + 1, length))
        else:
            print('Тест {0}: длина = {1}. Результат НЕ верный'.format(i + 1, length))
            count += 1
            in_out.print_array_in_row(arr)
            in_out.print_array_in_row(sorted_by_method_array)
    print('Тестирование завершено. Неверных тестов: ', count)


autotest(quick_sort)
