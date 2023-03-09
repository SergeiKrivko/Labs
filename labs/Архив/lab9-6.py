#   Кривко Сергей ИУ7-14Б
# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
# A, B, C и массив V

# Ввод матриц
while True:
    n = int(input('Введите размер квадратных матриц: '))
    if n > 0:
        break
    print('Размер матрицы должен быть натуральным числом')
A = []
print('Матрица A')
for i in range(n):
    A.append([])
    for j in range(n):
        A[i].append(int(input('Введите {0}-ый элемент {1}-ой строки матрицы A: '.format(j + 1, i + 1))))
B = []
print('Матрица B')
for i in range(n):
    B.append([])
    for j in range(n):
        B[i].append(int(input('Введите {0}-ый элемент {1}-ой строки матрицы B: '.format(j + 1, i + 1))))

# Составление матрицы C и массива V
C = []
V = [0] * n
for i in range(n):
    C.append([])
    for j in range(n):
        C[i].append(A[i][j] * B[i][j])
        V[j] += C[i][j]


# Вывод матрицы A
print('Матрица A')
for i in range(n):
    for j in range(n):
        print(' {0:5} '.format(A[i][j]), end='')
    print()
print()

# Вывод матрицы B
print('Матрица B')
for i in range(n):
    for j in range(n):
        print(' {0:5} '.format(B[i][j]), end='')
    print()
print()

# Вывод матрицы C
print('Матрица C')
for i in range(n):
    for j in range(n):
        print(' {0:5} '.format(C[i][j]), end='')
    print()
print()

# Вывод массива V
print('Массив V')
for i in range(n):
    print(' {0:5} '.format(V[i]), end='')
print()
