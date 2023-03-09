import os
import struct
import time


def heap_sort(array, func):
    n = len(array)
    a = array

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


def quick_sort(array, func):
    def partition(left, right):
        pivot = a[right]
        m = left
        for i in range(left, right):
            if func(a[i], pivot):
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

    a = array
    qsort(0, len(a) - 1)


def format_file_size(file_name):
    file_size = os.path.getsize(file_name)
    if file_size < 2 ** 11:
        return str(file_size) + ' ' + 'б'
    if file_size < 2 ** 21:
        return str(round(file_size / (2**10))) + ' ' + 'кб'
    if file_size < 2 ** 31:
        return str(round(file_size / (2**20))) + ' ' + 'Мб'
    return str(round(file_size / (2**30))) + ' ' + 'Гб'


def bwt(s):
    """Алгоритм Барроуза-Уилера (Burrows-Wheeler transform)"""
    length = len(s)
    initial_s = s
    array_of_permutations = [s]
    for i in range(1, length):
        s = bytes(s[-1:]) + s[:-1]
        array_of_permutations.append(s)

    array_of_permutations.sort()
    initial_str_index = array_of_permutations.index(initial_s)
    s_bwt = []
    for el in array_of_permutations:
        s_bwt.append(el[-1])
    return struct.pack(str(length) + 'B', *s_bwt), initial_str_index


def bwt2(s, sort='python'):
    """Алгоритм Барроуза-Уилера (Burrows-Wheeler transform)"""
    def comp(n1, n2):
        for i in range(length):
            if s[n1 + i] < s[n2 + i]:
                return True
            if s[n1 + i] > s[n2 + i]:
                return False
        return False

    length = len(s)
    s += s
    array = list(range(length))

    if sort == 'heap':
        heap_sort(array, comp)
    elif sort == 'quick':
        quick_sort(array, comp)
    else:
        array.sort(key=lambda i: s[i:i + length - 1])

    initial_str_index = array.index(0)
    s_bwt = []
    for el in array:
        s_bwt.append(s[el + length - 1])
    return struct.pack(str(length) + 'B', *s_bwt), initial_str_index


def bwt_decode(s, index):
    arr = list(s)
    for i in range(len(arr)):
        arr[i] = [arr[i]]
    first_column = list(s)
    for j in range(1, len(s)):
        arr.sort()
        for i in range(len(arr)):
            arr[i] = [first_column[i]] + arr[i]
    arr.sort()
    return bytes(arr[index])


def bwt_decode2(s, index):
    arr1 = list(s)
    arr2 = list(s)
    arr2.sort()
    for i in range(len(arr2)):
        arr2[i] = bytes([arr1[i], arr2[i]])
    arr = list(range(len(s)))
    arr.sort(key=lambda x: arr2[x])
    s_decoded = []
    for i in range(len(s)):
        s_decoded.append(arr2[arr[index]][0])
        index = arr[index]
    return bytes(s_decoded)


def rle(file, s, index):
    last_byte = s[0]
    packed_size = 0
    packed_s = b''
    count = 0
    pack_format = 'B'
    for el in s:
        if el != last_byte or count == 254:
            packed_s += struct.pack(pack_format + 'B', count, last_byte)
            packed_size += 2
            last_byte = el
            count = 1
        else:
            count += 1
    packed_s += struct.pack(pack_format + 'B', count, last_byte)
    packed_size += 2
    file.write(struct.pack('II', packed_size, index))
    file.write(packed_s)


def rle_decode(file, size):
    s_decode = b''
    for i in range(size // 2):
        count, byte = struct.unpack('Bs', file.read(2))
        s_decode += byte * count
        print(len(s_decode))
    return s_decode


def rle_smart(file, s, index):
    def check_next_3_bytes(index):
        if index > len(s) - 4:
            return False
        if s[index + 1] == s[index]:
            return False
        if s[index + 2] == s[index + 1]:
            return False
        if s[index + 3] == s[index + 2]:
            return False
        return True

    def check_next_2_bytes(index):
        if index > len(s) - 3:
            return True
        return s[index] == s[index + 1] and s[index] == s[index + 2]

    last_byte = s[0]
    packed_size = 0
    packed_s = b''
    count = 0
    flag = False

    for i in range(len(s)):
        if flag:
            if check_next_2_bytes(i) or count == 255:
                flag = False
                packed_s += struct.pack('B', 0) + struct.pack('B', count) + s[i - count:i]
                packed_size += 2 + count
                if check_next_3_bytes(i):
                    flag = True
                    count = 1
                else:
                    count = 1
                    last_byte = s[i]
            else:
                count += 1
        elif s[i] != last_byte:
            if count < 255:
                packed_s += struct.pack('BB', count, last_byte)
                packed_size += 2
            else:
                packed_s += struct.pack('B', 255) + struct.pack('H', count) + struct.pack('B', last_byte)
                packed_size += 6
            if check_next_3_bytes(i):
                flag = True
                count = 1
            else:
                count = 1
                last_byte = s[i]
        else:
            count += 1
    if count < 256:
        packed_s += struct.pack('BB', count, last_byte)
        packed_size += 2
    else:
        packed_s += struct.pack('B', 255) + struct.pack('H', count) + struct.pack('B', last_byte)
        packed_size += 6
    file.write(struct.pack('II', packed_size, index))
    file.write(packed_s)


def rle_smart_decode(file, packed_size):
    s_decode = b''

    unpacked_size = 0
    while unpacked_size < packed_size:
        count = struct.unpack('B', file.read(1))[0]
        if count == 0:
            count2 = struct.unpack('B', file.read(1))[0]
            # print('simple', count2)
            s_decode += struct.unpack(str(count2) + 's', file.read(count2))[0]
            unpacked_size += 2 + count2
        elif count == 255:
            count2 = struct.unpack('H', file.read(2))[0]
            byte = struct.unpack('s', file.read(1))[0]
            s_decode += byte * count2
            unpacked_size += 6
        else:
            byte = struct.unpack('s', file.read(1))[0]
            s_decode += byte * count
            unpacked_size += 2
    return s_decode


def pack(file1, file2, size=32766, sort='python', smart_rle=False, verbose=True, func=None):
    t = time.time()
    file1_size = os.path.getsize(file1)
    file1 = open(file1, 'br')
    file2 = open(file2, 'bw')
    if verbose:
        print('Процесс сжатия:  0%', end='')
    if func is not None:
        func(0)
    for i in range(file1_size // size + 1):
        s = file1.read(size)
        s, index = bwt2(s, sort)
        if smart_rle:
            rle_smart(file2, s, index)
        else:
            rle(file2, s, index)
        if verbose:
            print('\b\b\b{:2}%'.format(int(size * i / file1_size * 100)), end='')
        if func is not None:
            func(int(size * i / file1_size * 100))
    file1.close()
    file2.close()
    if verbose:
        print('\b\b\b100%')
        print('{0} => {1} ({2}%)'.format(format_file_size(file1.name), format_file_size(file2.name),
                                      round((os.path.getsize(file1.name) - os.path.getsize(file2.name)) /
                                            os.path.getsize(file1.name) * 100)))
        print('Время сжатия:', f'{time.time() - t:3f}')
    if func is not None:
        func(100)
        return format_file_size(file1.name), format_file_size(file2.name), \
            f'{round((os.path.getsize(file1.name) - os.path.getsize(file2.name)) / os.path.getsize(file1.name) * 100)}%', \
            time.time() - t


def unpack(file1, file2, verbose=True, func=None):
    if verbose:
        print('Процесс декодирования:  0%', end='')
    if func is not None:
        func(0)
    file1_size = os.path.getsize(file1)
    file1 = open(file1, 'br')
    file2 = open(file2, 'bw')
    current_position = 0
    while current_position < file1_size:
        packed_size, index = struct.unpack('II', file1.read(8))

        s_decode = rle_smart_decode(file1, packed_size)

        file2.write(bwt_decode2(s_decode, index))
        current_position += packed_size + 9
        if verbose:
            print('\b\b\b{:2}%'.format(int(current_position / file1_size * 100)), end='')
        if func is not None:
            func(int(current_position / file1_size * 100))
    file1.close()
    file2.close()


# file1 = 'test3.txt'
# file2 = 'test3-smart_rle.bin'
# file3 = 'test3-smart_rle-d.txt'
# pack(file1, file2, sort='quick, smart_rle=True)
# unpack(file2, file3)
