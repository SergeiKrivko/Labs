#   Кривко Сергей ИУ7-14Б
# 4: Переставить местами столбцы с максимальной и минимальной суммой
# элементов.


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


current_sum = 0                   # Сумма текущего столбца
max_sum = float('-inf')           # Максимальная сумма элементов столбца
min_sum = float('inf')            # Минимальная сумма элементов столбца
st_with_max_sum = 0               # Столбец с максимальной суммой
st_with_min_sum = 0               # Столбец с минимальной суммой

for j in range(n):                          # Проходим по столбцам матрицы
    current_sum = 0
    for i in range(m):                      # Считаем сумму каждого столбца
        current_sum += a[i][j]
    if current_sum > max_sum:               # Обновляем максимумы
        max_sum = current_sum
        st_with_max_sum = j
    if current_sum < min_sum:               # Обновляем минимумы
        min_sum = current_sum
        st_with_min_sum = j

# Меняем столбцы местами
for i in range(m):
    a[i][st_with_max_sum], a[i][st_with_min_sum] = a[i][st_with_min_sum], a[i][st_with_max_sum]

# Вывод матрицы
print()
for i in range(m):
    for j in range(n):
        print('{0:6} '.format(a[i][j]), end='')
    print()
