import struct
import os

SIZE = 4
def input_file_name_and_open_file():
    """
    Ввод имени файла
    :return: файл, имя файла
    """
    while True:
        file_name = input('Введите имя файла: ')
        try:
            f = open(file_name, 'bw')
            return f, file_name
        except PermissionError:
            print('Открыть файл невозможно: нет прав')
        except Exception:
            print('Открыть файл невозможно')


def open_file_and_write_numbers():
    """
    Ввод имени файла, открытие файла и ввод чисел
    :return: имя файла
    """
    file, file_name = input_file_name_and_open_file()
    print('Ввод чисел. Для окончания ввода нажмите Enter')
    while True:
        try:
            x = input('Введите число: ')
            if x == '':
                file.close()
                return file_name
            file.write(struct.pack('i', int(x)))
        except ValueError:
            print('Некорректное число')


def file_size(file_name):
    """
    Вычисление кол-ва чисел в файле
    :param file_name: Имя файла
    :return: кол-во чисел в файле
    """
    return os.path.getsize(file_name) // 4


def print_file(file_name):
    """
    Вывод чисел из файла в консоль
    :param file_name: имя файла
    """
    file = open(file_name, 'br')
    for i in range(file_size(file_name)):
        print(struct.unpack('i', file.read(4))[0])
