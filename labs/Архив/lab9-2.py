#   Кривко Сергей ИУ7-14Б
# Поворот квадратной матрицы


# Ввод матрицы
while True:
    n = int(input('Введите размер квадратной матрицы: '))
    if n > 0:
        break
    print('Размер матрицы должен быть натуральным числом')
a = []
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(int(input('Введите {0}-ый элемент {1}-ой строки: '.format(j + 1, i + 1))))

# Вывод матрицы
print()
for i in range(n):
    for j in range(n):
        print(' {0:5} '.format(a[i][j]), end='')
    print()
print()


# Поворот матрицы по часовой стрелке
for i in range(n // 2):
    for j in range(i, n - i - 1):
        a[i][j], a[j][n - i - 1], a[n - i - 1][n - j - 1], a[n - j - 1][i] = \
            a[n - j - 1][i], a[i][j], a[j][n - i - 1], a[n - i - 1][n - j - 1]


# Вывод матрицы
print()
for i in range(n):
    for j in range(n):
        print(' {0:5} '.format(a[i][j]), end='')
    print()
print()

# Поворот матрицы против часовой стрелки
for i in range(n // 2):
    for j in range(i, n - i - 1):
        a[i][j], a[j][n - i - 1], a[n - i - 1][n - j - 1], a[n - j - 1][i] = \
             a[j][n - i - 1], a[n - i - 1][n - j - 1], a[n - j - 1][i], a[i][j]


# Вывод матрицы
print()
for i in range(n):
    for j in range(n):
        print(' {0:5} '.format(a[i][j]), end='')
    print()
print()
