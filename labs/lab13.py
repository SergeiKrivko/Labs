import in_out
import menu
from database import DataBase


file_name = input('Введите имя файла: ')
data_base = DataBase(file_name, ['Фамилия', 'Имя', 'Возраст', 'Почта'], [str, str, int, str], [15, 15, 12, 40], sep=',')


def open_data_base():
    file_name = input('Введите имя файла: ')
    global data_base
    data_base = DataBase(file_name, ['Фамилия', 'Имя', 'Возраст', 'Почта'], [str, str, int, str],
                         [15, 15, 12, 40], sep=',')


def input_line_and_add(data_base):
    row = []
    for i in range(len(data_base.columns_format)):
        row.append(str(in_out.input_value('Введите значение поля "{0}"'.format(data_base.columns_names[i]),
                                            data_base.columns_format[i])))
    data_base.add_line(row)


def input_one_value_and_search(data_base):
    value = in_out.input_value('Введите значение поля "{0}" для поиска'.format(data_base.columns_names[0]),
                                data_base.columns_format[0])
    for row in data_base.search(value):
        for i in range(len(row)):
            print('| {0:{1}}'.format(row[i], data_base.column_width[i]), end='')
        print(' |')


def input_two_values_and_search(data_base):
    value1 = in_out.input_value('Введите значение поля "{0}" для поиска'.format(data_base.columns_names[0]),
                                data_base.columns_format[0])
    value2 = in_out.input_value('Введите значение поля "{0}" для поиска'.format(data_base.columns_names[1]),
                                data_base.columns_format[1])
    for row in data_base.two_column_search(value1, value2):
        for i in range(len(row)):
            print('| {0:{1}}'.format(row[i], data_base.column_width[i]), end='')
        print(' |')


menu.run_menu(('Выбрать файл для работы', open_data_base),
               ('Инициализировать базу данных', lambda: data_base.initialise()),
               ('Вывести содержимое базы данных', lambda: data_base.print_data_base()),
               ('Добавить запись', lambda: input_line_and_add(data_base)),
               ('Поиск по фамилии', lambda: input_one_value_and_search(data_base)),
               ('Поиск по фамилии и имени', lambda: input_two_values_and_search(data_base)))
