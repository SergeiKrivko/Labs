#   Кривко Сергей ИУ7-14Б
# 1: Поиск строки с наименьшим кол-вом четных элементов.

# Ввод матрицы
while True:
    m = int(input('Введите кол-во строк: '))
    if m > 0:
        break
    print('Кол-во строк должно быть положительным')
while True:
    n = int(input('Введите кол-во столбцов: '))
    if n > 0:
        break
    print('Кол-во столбцов должно быть положительным')
a = [[0]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        a[i][j] = int(input('Введите {0}-й элемент {1}-ой строки матрицы: '.format(i + 1, j + 1)))


current_count = 0                   # Кол-во четных элементов в текущей строке
min_count = float('inf')            # Минимальное кол-во четных элементов в одной строке
str_with_min_count = 0              # Строка с минимальным кол-вом четных элементов

for i in range(m):                  # Проходим по строкам матрицы
    current_count = 0
    for j in range(n):              # Считаем кол-во четных элементов
        if a[i][j] % 2 == 0:
            current_count += 1
    if current_count < min_count:       # Обновляем максимумы
        min_count = current_count
        str_with_min_count = i

# Вывод результата
print('{0}-ая строка матрицы: {1} четных элементов'.format(str_with_min_count + 1, min_count))
for j in a[str_with_min_count]:
    print(j, ', ', sep='', end='')
print('\b\b')
