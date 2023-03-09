import random


def heap_sort(array, func):
    n = len(array)
    a = array.copy()

    def heapify(arr, n, i, func):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and func(arr[i], arr[l]):
            largest = l
        if r < n and func(arr[largest], arr[r]):
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest, func)

    for i in range(n, -1, -1):
        heapify(a, n, i, func)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0, func)
    return a


def comp(s1, s2, alph):
    for i in range(len(s1)):
        if alph.index(s1[i]) < alph.index(s2[i]):
            return True
        elif alph.index(s1[i]) > alph.index(s2[i]):
            return False


def find_symbol(alph):
    i = 33
    while chr(i) in alph:
        if i == 47:
            i += 9
        i += 1
    return chr(i)


def bwt(s, alph):
    """Алгоритм Барроуза-Уилера (Burrows-Wheeler transform)"""
    symbol = find_symbol(alph)
    alph = alph + [symbol]
    s += symbol
    length = len(s)
    array_of_permutations = []
    for i in range(length):
        array_of_permutations.append(s)
        s = s[-1] + s[:-1]

    array_of_permutations = heap_sort(array_of_permutations, lambda s1, s2: comp(s1, s2, alph))
    s_bwt = ''
    for el in array_of_permutations:
        s_bwt += el[-1]
        # print(el)
    return s_bwt


def bwt_decode(s, alph):
    symbol = find_symbol(alph)
    alph = alph + [symbol]
    arr = list(s)
    first_column = list(s)
    for j in range(1, len(s)):
        sorted_arr = heap_sort(arr, lambda s1, s2: comp(s1, s2, alph))
        for i in range(len(arr)):
            arr[i] = first_column[i] + sorted_arr[i]
    for el in arr:
        if el[-1] == symbol:
            return el[:-1]


def bwt2(s, alph):
    def str_is_less_then(n1, n2):
        for i in range(n):
            if alph.index(s[n1 + i]) > alph.index(s[n2 + i]):
                return True
            elif alph.index(s[n1 + i]) < alph.index(s[n2 + i]):
                return False
        return False

    symbol = find_symbol(alph)
    n = len(s) + 1
    alph = alph + [symbol]
    s = s + symbol + s + symbol
    min_str = 0
    max_str = 0
    for i in range(n):
        if str_is_less_then(i, min_str):
            min_str = i
        elif not str_is_less_then(i, max_str):
            max_str = i
    # print('min_str', s[min_str:min_str + n])
    # print('max_str', s[max_str:max_str + n])
    s_bwt = [s[max_str + n - 1]]
    last_str = max_str
    for i in range(1, n):
        max_str = min_str
        for j in range(1, n):
            if str_is_less_then(j, last_str) and not str_is_less_then(j, max_str):
                max_str = j
        last_str = max_str
        s_bwt.append(s[max_str + n - 1])
    return ''.join(s_bwt)


# alph = list('abcdefghijklmnopqrstuvwxyz')
# f = open('test.txt', 'w')
# for i in range(1000):
#     f.write(alph[random.randint(0, len(alph) - 1)])
# f.close()
# f = open('test.txt')
# a = f.read()
# # print(a)
# # print(bwt(a, ['a', 'b', 'c']))
# print(bwt2(a, alph))
