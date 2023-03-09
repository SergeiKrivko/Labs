#   Кривко Сергей ИУ7-14Б
# Умножение матриц.

# Ввод матрицы
while True:
    n = int(input('Введите размер квадратых матриц: '))
    if n > 0:
        break
    print('Размер должен быть положительным')
print('Матрица 1')
a = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input('Введите {0}-й элемент {1}-ой строки матрицы: '.format(i + 1, j + 1)))
print('Матрица 2')
b = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        b[i][j] = int(input('Введите {0}-й элемент {1}-ой строки матрицы: '.format(i + 1, j + 1)))

c = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        s = 0
        for k in range(n):
            s += a[i][k] * b[k][j]
        c[i][j] = s

# Вывод результата
print()
for i in range(n):
    print('|', end='')
    for j in range(n):
        print('{0:4} '.format(a[i][j]), end='')
    print('|       |', end='')
    for j in range(n):
        print('{0:4} '.format(b[i][j]), end='')
    print('|       |', end='')
    for j in range(n):
        print('{0:4} '.format(c[i][j]), end='')
    print('|')
