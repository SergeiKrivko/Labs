from database import DataBaseBin
from menu import menu
import in_out


def command_open():
    global data_base
    data_base = DataBaseBin(input('Введите имя файла: '), ['Фамилия', 'Имя', 'Возраст', 'Почта'],
                                                          [str, str, int, str],
                                                          [20, 20, 4, 40])


def command_add_line(data_base):
    index = in_out.input_value('Введите индекс')
    data_base.add_row(data_base.input_row())


def command_search(data_base):
    pass


def command_search2(data_base):
    pass


menu(('Выбрать файл', command_open),
     ('Инициализировать файл', lambda: data_base.clear()),
     ('Напечатать содержимое', lambda: data_base.print()),
     ('Добавить запись', lambda: command_add_line(data_base)),
     ('Поиск по фамилии', lambda: command_search(data_base)),
     ('Поиск по фамилии и имени', lambda: command_search2(data_base)))
