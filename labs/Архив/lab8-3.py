#   Кривко Сергей ИУ7-14Б
# 3: Поиск столбца с наибольшим количеством чисел, являющихся степенями 2.

import math

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


current_count = 0                   # Кол-во степеней 2 в текущем столбце
max_count = 0                       # Максимальное кол-во степеней 2 в одном столбце
st_with_max_count = 0               # Столбец с наибольшим количеством чисел, являющихся степенями 2

for j in range(n):              # Проходим по столбцам матрицы
    current_count = 0
    for i in range(m):          # Проходим по элементам столбца матрицы
        if a[i][j] > 0 and math.log2(a[i][j]) % 1 == 0:             # Считаем кол-во элементов, равных степени 2
            current_count += 1
    if current_count > max_count:           # Обновляем максимумы
        max_count = current_count
        st_with_max_count = j

# Вывод результата
print('{0}-ый столбец матрицы: {1} чисел, являющихся степенями 2'.format(st_with_max_count + 1, max_count))
for i in a:
    print(i[st_with_max_count], ', ', sep='', end='')
print('\b\b')
