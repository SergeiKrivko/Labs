#   Кривко Сергей ИУ7-14Б
# Замена в матрице символов всех гласных английских букв на точки


# Ввод матрицы
while True:
    m = int(input('Введите кол-во строк матрицы: '))
    if m > 0:
        break
    print('Размер матрицы должен быть натуральным числом')
while True:
    n = int(input('Введите кол-во столбцов матрицы: '))
    if n > 0:
        break
    print('Размер матрицы должен быть натуральным числом')
A = []
for i in range(m):
    A.append([])
    for j in range(n):
        A[i].append(input('Введите {0}-ый элемент {1}-ой строки матрицы A: '.format(j + 1, i + 1)))

# Вывод матрицы
print()
for i in range(m):
    for j in range(n):
        print(A[i][j], end=' ')
    print()

for i in range(m):      # Проходим по матрице
    for j in range(n):
        if A[i][j] in 'aeiouyAEIOUY':
            A[i][j] = '.'

# Вывод матрицы
print()
for i in range(m):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
