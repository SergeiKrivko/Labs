#   Кривко Сергей, ИУ7-14Б
# Удаление всех положительных чисел из файла


import struct
import lab15


file_name = lab15.open_file_and_write_numbers()


size = lab15.file_size(file_name)

file = open(file_name, 'br+')       # Открытие файла
right = 0                           # Правая граница
left = 0                            # Левая граница
while right < size:
    file.seek(right * 4)
    value = struct.unpack('i', file.read(4))[0]         # Читаем число из файла
    if value > 0:                                       # Если оно положительное, сдвигаем правую границу
        right += 1
    else:                                               # Иначе копируем это число на левую границу, сдвигаем обе гр.
        file.seek(left * 4)
        file.write(struct.pack('i', value))
        right += 1
        left += 1
file.truncate(left * 4)                     # Обрезаем файл

file.close()


lab15.print_file(file_name)
