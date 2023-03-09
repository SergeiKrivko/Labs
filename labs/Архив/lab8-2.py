#   Кривко Сергей ИУ7-14Б
# 2: Переставить местами строки с наибольшим и наименьшим количеством
# отрицательных элементов.

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


current_count = 0                   # Кол-во отрицательных элементов в текущей строке
min_count = float('inf')            # Минимальное кол-во отрицательных элементов в одной строке
max_count = 0                       # Максимальное кол-во отрицательных элементов в одной строке
str_with_min_count = 0              # Строка с минимальным кол-вом отрицательных элементов
str_with_max_count = 0              # Строка с максимальным кол-вом отрицательных элементов


for i in range(m):                          # Проходим по строкам матрицы
    current_count = 0
    for j in range(n):                      # Проходим по элементам строки матрицы
        if a[i][j] < 0:                     # Считаем кол-во отрицательных элементов
            current_count += 1
    if current_count < min_count:           # Обновляем максимумы
        min_count = current_count
        str_with_min_count = i
    if current_count > max_count:           # Обновляем минимумы
        max_count = current_count
        str_with_max_count = i

# Меняем строки местами
a[str_with_min_count], a[str_with_max_count] = a[str_with_max_count], a[str_with_min_count]


# Вывод матрицы
for i in range(m):
    for j in range(n):
        print('{0:6} '.format(a[i][j]), end='')
    print()