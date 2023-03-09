#   Кривко Сергей, ИУ7-14Б
# База данных

import in_out


columns_names = ['Фамилия', 'Имя', 'Возраст', 'Почта']      # Названия полей
columns_format = [str, str, int, str]                       # Формат полей
column_width = [20, 20, 12, 40]                             # Ширина полей при печати
file, file_name = None, ''


def open_data_base():
    """Ввод имени файла и поиск"""
    file_name = input('Введите имя файла: ')
    try:
        f = open(file_name, 'r+')
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


def print_data_base(file, column_width):
    """Вывод базы данных"""
    if file is None:
        print('Ошибка: файл не существует')
        return
    file.seek(0)
    i = 0
    for line in file:
        a = line.strip().split(',')
        if len(a) != len(column_width):
            print('| Запись повреждена', ' ' * 80, end='')
        else:
            for i in range(len(column_width)):
                if len(a[i]) < column_width[i]:
                    print('| {0:{1}}'.format(a[i], column_width[i]), end='')
                else:
                    print('| {0}…'.format(a[i][:column_width[i] - 1]), end='')
        print(' |')
        i += 1
    if i == 0:
        print('Файл пуст')


def initialise(file, file_name):
    """Инициализация базы данных"""
    if file_name == '':
        print('Операция невозможна: имя файла не задано.')
        return
    try:
        file.close()
    except AttributeError:
        pass
    try:
        file = open(file_name, mode='a+')
        return file
    except Exception:
        print('Создать файл невозможно')


def add_line(file, row):
    """Добавление записи"""
    file.seek(0, 2)
    file.write(','.join(map(str, row)))
    file.write('\n')


def search(file, value):
    """Поиск в базе"""
    file.seek(0)
    res = []
    for line in file:
        try:
            a = line.split(',')
            for i in range(len(a)):
                a[i] = columns_format[i](a[i].strip())
            if a[0] == value:
                res.append(a)
        except Exception:
            pass
    return res


def two_column_search(file, value1, value2):
    """Поиск в базе по двум полям"""
    file.seek(0)
    res = []
    for line in file:
        try:
            a = line.split(',')
            for i in range(len(a)):
                a[i] = columns_format[i](a[i].strip())
            if a[0] == value1 and a[1] == value2:
                res.append(a)
        except Exception:
            pass
    return res


def input_line_and_add(file, columns_format, columns_names):
    """Ввод и добавление записи"""
    if file is None:
        print('Ошибка: файл не существует')
        return
    row = []
    for i in range(len(columns_format)):
        row.append(str(in_out.input_value('Введите значение поля "{0}"'.format(columns_names[i]), columns_format[i])))
    add_line(file, row)


def input_one_value_and_search(file, columns_format, columns_names):
    """Ввод значения первого поля и поиск по нему"""
    if file is None:
        print('Ошибка: файл не существует')
        return
    value = in_out.input_value('Введите значение поля "{0}" для поиска'.format(columns_names[0]), columns_format[0])
    res = search(file, value)       # Результат поиска
    if len(res) == 0:
        print('Ничего не найдено')
    else:           # Выводим результат
        for row in res:
            for i in range(len(row)):
                print('| {0:{1}}'.format(row[i], column_width[i]), end='')
            print(' |')


def input_two_values_and_search(file, columns_format, columns_names):
    """Ввод значений первого и второго полей и поиск"""
    if file is None:
        print('Ошибка: файл не существует')
        return
    value1 = in_out.input_value('Введите значение поля "{0}" для поиска'.format(columns_names[0]),
                                columns_format[0])
    value2 = in_out.input_value('Введите значение поля "{0}" для поиска'.format(columns_names[1]),
                                columns_format[1])
    res = two_column_search(file, value1, value2)       # Результат поиска
    if len(res) == 0:
        print('Ничего не найдено')
    else:           # Выводим результат
        for row in res:
            for i in range(len(row)):
                print('| {0:{1}}'.format(row[i], column_width[i]), end='')
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
            ('Вывести содержимое базы данных', lambda: print_data_base(file, column_width)),
            ('Добавить запись', lambda: input_line_and_add(file, columns_format, columns_names)),
            ('Поиск по фамилии', lambda: input_one_value_and_search(file, columns_format, columns_names)),
            ('Поиск по фамилии и имени', lambda: input_two_values_and_search(file, columns_format, columns_names))]

while True:
    print_menu(commands)
    command = input_command(commands)
    if command == 1:
        file, file_name = commands[command][1]()
    elif command == 2:
        file = commands[command][1]()
    else:
        commands[command][1]()  # Вызов команды
