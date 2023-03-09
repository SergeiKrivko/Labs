#   Кривко Сергей, ИУ7-14Б
# База данных на бинарных файлах

import in_out
import struct
import os


columns_names = ['Фамилия', 'Имя', 'Возраст', 'Почта']      # Названия полей
columns_format = [str, str, int, str]                       # Формат полей
column_size = [20, 20, 4, 40]                             # Ширина полей при печати
row_size = 84
pack_format = '20s20si40s'


def open_data_base():
    """Ввод имени файла и поиск"""
    file_name = input('Введите имя файла: ')
    try:
        f = open(file_name, 'br+')
        return f, file_name
    except FileNotFoundError:
        print('Файл не найден. Вы можете создать его командой 2')
        return None, file_name
    except PermissionError:
        print('Открыть файл невозможно: нет прав')
        return None, None
    except Exception:
        print('Открыть файл невозможно')
        return None, None


def print_data_base(file):
    """Вывод базы данных"""
    if file_size(file_name) == 0:
        print('Файл пуст')
        return
    if file is None:
        print('Ошибка: файл не существует')
        return
    try:
        file.seek(0)
        for _ in range(file_size(file_name)):
            row = read_row(file)
            for i in range(len(row)):
                if columns_format[i] == int or columns_format[i] == float:
                    print('| {0:10.5g}'.format(row[i]), end='')
                else:
                    print('| {0:{1}}'.format(row[i], column_size[i]), end='')
            print(' |')
    except Exception:
        print('Файл поврежден')


def read_row(file):
    """Чтение одной записи"""
    a = struct.unpack(pack_format, file.read(row_size))
    row = []
    for i in range(len(a)):
        if columns_format[i] == str:
            row.append(a[i].decode('utf-8').strip())
        else:
            row.append(a[i])
    return row


def initialise(file, file_name):
    """Инициализация базы данных"""
    if file_name == '':
        print('Операция невозможна: имя файла не задано.')
        return
    try:
        file = open(file_name, mode='bw')
        file.close()
        file = open(file_name, mode='br+')
        return file
    except Exception:
        print('Создать файл невозможно')


def input_row():
    """Ввод записи с клавиатуры"""
    row = []
    for i in range(len(columns_format)):
        while True:
            a = (in_out.input_value('Введите значение поля "{}"'.format(columns_names[i]),
                                    columns_format[i]))
            if columns_format[i] == str and len(a) > column_size[i]:
                print('Слишком длинное значение')
            elif columns_format[i] == int and abs(a) > 2 ** (8 * column_size[i] - 1):
                print('Слишком большое число')
            else:
                row.append(a)
                break
    return row


def file_size(file_name):
    """Вычисляет размер файла"""
    return os.path.getsize(file_name) // row_size


def add_line(file, row, index):
    """Добавление записи"""
    for i in range(len(row)):
        if isinstance(row[i], str):
            row[i] = '{:{}}'.format(row[i], column_size[i]).encode('utf-8')
    file.seek(0, 2)
    if index:
        for i in range(file_size(file_name), index, -1):
            file.seek(-row_size, 1)
            r = file.read(row_size)
            file.write(r)
            file.seek((-2) * row_size, 1)
    file.write(struct.pack(pack_format, *row))


def remove_line(file, index):
    file.seek(index * row_size)
    for i in range(index, file_size(file_name)):
        r = file.read(row_size)
        file.seek((-2) * row_size, 1)
        file.write(r)
        file.seek(row_size, 1)
    file.truncate(os.path.getsize(file_name) - row_size)


def search(file, value):
    """Поиск в базе данных по первому полю"""
    file.seek(0)
    res = []
    for _ in range(file_size(file_name)):
        row = read_row(file)
        if row[0] == value:
            res.append(row)
    return res


def two_column_search(file, value1, value2):
    """Поиск в базе данных по первым двум полям"""
    file.seek(0)
    res = []
    for _ in range(file_size(file_name)):
        row = read_row(file)
        if row[0] == value1 and row[1] == value2:
            res.append(row)
    return res


def input_line_and_add(file):
    """Ввод и добавление записи"""
    if file is None:
        print('Ошибка: файл не существует')
        return
    index = in_out.input_value('Введите индекс для вставки (Если введенный индекс больше кол-во записей, запись'
                               'будет добавлена в конец', only_positive=True)
    row = input_row()
    try:
        add_line(file, row, index)
    except Exception:
        print('Файл поврежден')


def input_one_value_and_search(file):
    """Ввод значения первого поля и поиск по нему"""
    if file is None:
        print('Ошибка: файл не существует')
        return
    value = in_out.input_value('Введите значение поля "{0}" для поиска'.format(columns_names[0]), columns_format[0])
    try:
        res = search(file, value)       # Результат поиска
    except Exception:
        print('Файл поврежден')
        return
    if len(res) == 0:
        print('Ничего не найдено')
    else:           # Выводим результат
        for row in res:
            for i in range(len(row)):
                if columns_format[i] == int or columns_format[i] == float:
                    print('| {0:10.5g}'.format(row[i]), end='')
                else:
                    print('| {0:{1}}'.format(row[i], column_size[i]), end='')
            print(' |')


def command_remove_line(file):
    """Ввод индекса и удаление записи"""
    if file is None:
        print('Ошибка: файл не существует')
        return
    index = in_out.input_value('Введите индекс для вставки', only_positive=True)
    if index > file_size(file_name):
        print('Такой записи не существует')
        return
    try:
        remove_line(file, index)
    except Exception:
        print('Файл поврежден')


def input_two_values_and_search(file):
    """Ввод значений первого и второго полей и поиск"""
    if file is None:
        print('Ошибка: файл не существует')
        return
    value1 = in_out.input_value('Введите значение поля "{0}" для поиска'.format(columns_names[0]),
                                columns_format[0])
    value2 = in_out.input_value('Введите значение поля "{0}" для поиска'.format(columns_names[1]),
                                columns_format[1])
    try:
        res = two_column_search(file, value1, value2)       # Результат поиска
    except Exception:
        print('Файл поврежден')
        return
    if len(res) == 0:
        print('Ничего не найдено')
    for row in res:
        for i in range(len(row)):
            if columns_format[i] == int or columns_format[i] == float:
                print('| {0:10.5g}'.format(row[i]), end='')
            else:
                print('| {0:{1}}'.format(row[i], column_size[i]), end='')
        print(' |')


def print_menu(commands):
    """Вывод списка команд на экран"""
    print()
    for i in range(len(commands)):
        print('{0}: {1}'.format(i, commands[i][0]))


def input_command(commands):
    """Ввод команды"""
    while True:
        try:
            c = int(input('Введите команду: '))
            if c < 0 or c >= len(commands):
                raise ValueError
            return c
        except ValueError:
            print('Некорректная команда')


commands = [('Завершить работу программы', exit),
            ('Выбрать файл для работы', open_data_base),
            ('Инициализировать базу данных', lambda: initialise(file, file_name)),
            ('Вывести содержимое базы данных', lambda: print_data_base(file)),
            ('Добавить запись', lambda: input_line_and_add(file)),
            ('Удалить запись', lambda: command_remove_line(file)),
            ('Поиск по фамилии', lambda: input_one_value_and_search(file)),
            ('Поиск по фамилии и имени', lambda: input_two_values_and_search(file))]

while True:
    print_menu(commands)
    command = input_command(commands)
    if command == 1:
        file, file_name = commands[command][1]()
    elif command == 2:
        file = commands[command][1]()
    else:
        commands[command][1]()  # Вызов команды
