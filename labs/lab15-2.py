#   Кривко Сергей, ИУ7-14Б
# Добавление после отрицательных элементов их удвоенных значений


import struct
import lab15


file_name = lab15.open_file_and_write_numbers()


size = lab15.file_size(file_name)
file = open(file_name, 'br+')

count = 0           # Кол-во отрицательных чисел в файле

# Считаем кол-во отрицательных чисел в файле
for i in range(size):
    value = struct.unpack('i', file.read(4))[0]
    if value < 0:
        count += 1

# Добавляем в конец файла нули
null = struct.pack('i', 0)
for i in range(count):
    file.write(null)

# Проходим по файлу
pos = size + count - 1              # Позиция для вставки
for i in range(size - 1, -1, -1):
    file.seek(i * 4)
    value = struct.unpack('i', file.read(4))[0]
    if value < 0:
        file.seek((pos - 1) * 4)
        file.write(struct.pack('i', value))
        file.write(struct.pack('i', value * 2))
        pos -= 2
    else:
        file.seek(pos * 4)
        file.write(struct.pack('i', value))
        pos -= 1

file.close()


lab15.print_file(file_name)
