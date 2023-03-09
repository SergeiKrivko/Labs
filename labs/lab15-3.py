#   Кривко Сергей, ИУ7-14Б
# Сор

import struct
import lab15


file_name = lab15.open_file_and_write_numbers()


def read_number_from_file(file, index):
    """
    Чтение числа из файла по индексу
    :param file: файл
    :param index: индекс
    :return: число
    """
    file.seek(index * 4)
    return struct.unpack('i', file.read(4))[0]


def write_number_to_file(file, index, value):
    """
    Замена числа в файле по индексу
    :param file: файл
    :param index: индекс
    :param value: новое число
    :return:
    """
    file.seek(index * 4)
    file.write(struct.pack('i', value))


def barrier_insertion_sort(file, size):
    """
    Сортировка чисел в файле методом вставок с барьером
    :param file: файл
    :param size: размер файла
    :return:
    """
    file.seek(0, 2)
    for i in range(size):
        file.seek(-4, 1)
        value = file.read(4)
        file.write(value)
        file.seek(-8, 1)
    write_number_to_file(file, 0, 0)
    for i in range(2, size + 1):
        if read_number_from_file(file, i - 1) > read_number_from_file(file, i):
            file.seek(0)
            write_number_to_file(file, 0, read_number_from_file(file, i))
            j = i - 1
            while read_number_from_file(file, j) > read_number_from_file(file, 0):
                write_number_to_file(file, j + 1, read_number_from_file(file, j))
                j -= 1
            write_number_to_file(file, j + 1, read_number_from_file(file, 0))
    file.seek(4)
    for i in range(size):
        r = file.read(4)
        file.seek(-8, 1)
        file.write(r)
        file.seek(4, 1)
    file.truncate(size * 4)


file = open(file_name, 'br+')

barrier_insertion_sort(file, lab15.file_size(file_name))
file.close()


lab15.print_file(file_name)
