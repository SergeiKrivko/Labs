# Даны 2 текстовых файла in1.txt и in2.txt.
# В первом файле записано N целых чисел со значениями от 1 до 3000 по одному в строке. Во втором файле записаны целые
# числа от 1 до N в произвольном порядке - номера строк в первом файле.
# Требуется сформировать файл out1.txt, в который записать числа из файла in1.txt, переведённые в римскую систему
# счисления, с выравниванием по центру (на основе длины числа с самым большим количеством цифр в римской с/с).
# Далее требуется сформировать файл out2.txt, переписав в него строки из файла out1.txt на основе порядка,
# заданного в файле in2.txt.
# Не разрешается считывать в память более одной строки каждого файла одновременно.

file_in1 = open('in1.txt')

alph = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def convert_to_rome_cistem(x):
    s = ''
    for item in alph:
        while x >= item[0]:
            s += item[1]
            x -= item[0]
    return s


max_len = 0

for line in file_in1:
    max_len = max(max_len, len(convert_to_rome_cistem(int(line))))


file_in1.seek(0)
file_out1 = open('out1.txt', 'w')


for line in file_in1:
    file_out1.write('{0:^{1}}'.format(convert_to_rome_cistem(int(line)), max_len) + '\n')

file_in1.close()
file_out1.close()
max_len += 1

file_in2 = open('in2.txt')
file_out1 = open('out1.txt')
file_out2 = open('out2.txt', 'w')

for line in file_in2:
    file_out1.seek((int(line) - 1) * (max_len + 1))
    a = file_out1.read(max_len)
    file_out2.write(a)
