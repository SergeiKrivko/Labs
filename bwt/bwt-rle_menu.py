import bwt_rle
from menu import menu
import in_out


use_heap_sort = True
use_smart_rle = True
size = 32


def command_modify_params():
    def command_set_size():
        global size
        size = in_out.input_value('Введите размер участков разбиения в килобайтах', only_positive=True)

    def command_set_heap_sort():
        def set_python_sort():
            global sort
            sort = 'python'

        def set_heap_sort():
            global sort
            sort = 'heap'

        def set_quick_sort():
            global sort
            sort = 'quick'

        menu(('heap sort', set_heap_sort, exit),
             ('quick sort', set_quick_sort, exit),
             ('python sort', set_python_sort, exit),
             command_exit_name='Отмена')

    def command_set_smart_rle():
        def set_smart_rle_true():
            global use_smart_rle
            use_smart_rle = True

        def set_smart_rle_false():
            global use_smart_rle
            use_smart_rle = False

        menu(('Использовать smart rle', set_smart_rle_true, exit),
             ('Не использовать smart rle', set_smart_rle_false, exit),
             command_exit_name='Отмена')

    menu(('Размер участков разбиения', command_set_size),
         ('Выбрать метод сортировки', command_set_heap_sort),
         ('Использовать/не использовать smart rle', command_set_smart_rle),
         command_exit_name='Назад')


def command_start_packing(file1, file2):
    bwt_rle.pack(file1, file2, size=(size * 1024), sort=sort, smart_rle=use_smart_rle)


def command_pack():
    while True:
        file1_name = input('Введите имя исходного файла: ')
        try:
            f = open(file1_name, 'br')
            f.close()
            break
        except FileNotFoundError:
            print('Файл не найден')
        except PermissionError:
            print('Не удалось открыть файл: нет прав')
        except Exception:
            print('Не удалось открыть файл')
    while True:
        file2_name = input('Введите имя конечного файла: ')
        try:
            f = open(file2_name, 'bw')
            f.close()
            break
        except PermissionError:
            print('Не удалось создать файл: нет прав')
        except Exception:
            print('Не удалось создать файл')
    menu(('Настроить параметры', command_modify_params),
         ('Сжать', lambda: command_start_packing(file1_name, file2_name), exit),
         command_exit_name='Отмена')


def command_unpack():
    while True:
        file1_name = input('Введите имя исходного файла: ')
        try:
            f = open(file1_name, 'br')
            f.close()
            break
        except FileNotFoundError:
            print('Файл не найден')
        except PermissionError:
            print('Не удалось открыть файл: нет прав')
        except Exception:
            print('Не удалось открыть файл')
    while True:
        file2_name = input('Введите имя конечного файла: ')
        try:
            f = open(file2_name, 'bw')
            f.close()
            break
        except PermissionError:
            print('Не удалось создать файл: нет прав')
        except Exception:
            print('Не удалось создать файл')
    bwt_rle.unpack(file1_name, file2_name)


menu(('Сжать файл', command_pack),
     ('Распаковать файл', command_unpack))
