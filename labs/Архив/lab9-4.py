#   Кривко Сергей ИУ7-14Б
# Определение максимума для заданных строк матрицы


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
# Ввод массива I
while True:
    l = int(input('Введите кол-во элементов массива I: '))
    if l > 0:
        break
    print('Размер массива должен быть натуральным числом')
I = []
for i in range(l):
    while True:
        x = int(input('Введите {0}-ый элемент массива I: '.format(i + 1)))
        if 1 <= x <= m:
            I.append(x - 1)
            break
        print('В матрице D нет такой строки')


R = [0] * l         # Массив максимумов строк матрицы D
sum_R = 0              # Сумма элементов массива D
count_R = 0            # Кол-во элементов массива D (кроме None)

# Проходим по массиву I, и для каждого элемента, являющегося индексом строки, находим максимум
for j in range(l):
    if 0 <= I[j] < m:
        current_max = D[I[j]][0]        # Текущий максимум
        for k in range(1, n):
            current_max = max(current_max, D[I[j]][k])
        R[j] = current_max

# Вывод матрицы D
print()
for i in range(m):
    for j in range(n):
        print(' {0:5} '.format(D[i][j]), end='')
    print()
print()

# Вывод массивов I и R
print('массив I  массив R')
for j in range(l):
    print('{0:7}   {1}'.format(I[j] + 1, R[j]))
