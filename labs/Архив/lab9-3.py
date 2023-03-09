#   Кривко Сергей ИУ7-14Б
# Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z


# Ввод матрицы D
while True:
    m = int(input('Введите кол-во строк матрицы D: '))
    if m > 0:
        break
    print('Размер матрицы должен быть натуральным числом')
while True:
    n = int(input('Введите кол-во столбцов матрицы D: '))
    if n > 0:
        break
    print('Размер матрицы должен быть натуральным числом')
D = []
for i in range(m):
    D.append([])
    for j in range(n):
        D[i].append(int(input('Введите {0}-ый элемент {1}-ой строки матрицы D: '.format(j + 1, i + 1))))
# Ввод матрицы Z
print('Кол-во строк матрицы Z =', m)
while True:
    n2 = int(input('Введите кол-во столбцов матрицы Z: '))
    if n2 > 0:
        break
    print('Размер матрицы должен быть натуральным числом')
Z = []
for i in range(m):
    Z.append([])
    for j in range(n2):
        Z[i].append(int(input('Введите {0}-ый элемент {1}-ой строки матрицы Z: '.format(j + 1, i + 1))))

# Вывод матрицы D
print('\nМатрица D\n')
for i in range(m):
    for j in range(n):
        print(' {0:5} '.format(D[i][j]), end='')
    print()
print()
# Вывод матрицы Z
print('\nМатрица Z\n')
for i in range(m):
    for j in range(n2):
        print(' {0:5} '.format(Z[i][j]), end='')
    print()
print()


G = [0] * m    # Массив количеств элементов в каждой строке матрицы D, превышающих суммы соответствующих строк матрицы Z
max_value = 0       # Максимальный элемент массива G
for i in range(m):
    current_sum = 0         # Сумма элементов текущей строки
    for j in range(n2):
        current_sum += Z[i][j]
    current_count = 0       # Кол-во элементов, превышающих current_sum, в текущей строке
    for j in range(n):
        if D[i][j] > current_sum:
            current_count += 1
    G[i] = current_count
    max_value = max(max_value, current_count)

# Умножаем матрицу D на max_value
for i in range(m):
    for j in range(n):
        D[i][j] *= max_value

# Вывод матрицы D и массива G
print('\nМатрица D и массив G\n')
for i in range(m):
    for j in range(n):
        print(' {0:5} '.format(D[i][j]), end='')
    print('          ', G[i])
print()
