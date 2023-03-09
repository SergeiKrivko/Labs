#   Кривко Сергей ИУ7-14Б
# 3: Поиск строки с наибольшим числом идущих подряд цифр.

# Ввод списка
while True:
    n = int(input('Введите длину списка: '))
    if n > 0:
        break
    print('Длина списка должна быть положительной')
a = []
for i in range(n):
    a.append(input('Введите {0}-ю строку списка: '.format(i + 1)))

current_len = 0                     # Длина текущей последовательности цифр
max_len_in_current_str = 0          # Максимальное кол-во подряд идущих цифр в текущей строке
str_with_max_len = 0                # Строка с максимальным кол-вом подряд идущих цифр
max_len = 0                         # Максимальное кол-во подряд идущих цифр

for i in range(n):                  # Проходим циклом по всем строкам
    current_len = 0                 # Обнуляем переменные
    max_len_in_current_str = 0
    for j in a[i]:                  # Проходим циклом по всем символам текущей строки
        if j in '1234567890':       # Если символ - цифра
            current_len += 1        # увеличиваем текущую длину на 1
            max_len_in_current_str = max(max_len_in_current_str, current_len)   # Обновляем максимум для данной строки
        else:
            current_len = 0         # Если символ - не цифра, то обнуляем текущую длину
    if max_len_in_current_str > max_len:        # Обновляем общие максимумы
        max_len = max_len_in_current_str
        str_with_max_len = i

# Выводим результат
if max_len == 0:
    print('Ни в одной строке нет цифр')
else:
    print('a[{0}]:'.format(str_with_max_len + 1), a[str_with_max_len], '({0} цифр подряд)'.format(max_len))
