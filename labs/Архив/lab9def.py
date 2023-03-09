#   Кривко Сергей ИУ7-14Б
# Нахождение среднего арифметического четных элементов подматрицы, определяемой максимальным и минимальным элементами
# исходной матрицы

# Ввод матрицы
while True:
    n = int(input('Введите кол-во строк матрицы: '))
    if n > 0:
        break
    print('Кол-во строк должно быть натуральным числом')
while True:
    m = int(input('Введите кол-во столбцов матрицы: '))
    if n > 0:
        break
    print('Кол-во столбцов должно быть натуральным числом')
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(int(input('Введите {0}-ый элемент {1}-ой строки: '.format(j + 1, i + 1))))

max_elem = a[0][0]
max_elem_i = 0
max_elem_j = 0
min_elem = a[0][0]
min_elem_i = 0
min_elem_j = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > max_elem:
            max_elem = a[i][j]
            max_elem_i = i
            max_elem_j = j
        if a[i][j] < min_elem:
            min_elem = a[i][j]
            min_elem_i = i
            min_elem_j = j

b = []
k = 0
summa = 0
count = 0
for i in range(min(min_elem_i, max_elem_i), max(min_elem_i, max_elem_i) + 1):
    b.append([])
    for j in range(min(min_elem_j, max_elem_j), max(min_elem_j, max_elem_j) + 1):
        b[k].append(a[i][j])
        if a[i][j] % 2 == 0:
            summa += a[i][j]
            count += 1
    k += 1

print('Исходная матрица')
for i in range(n):
    for j in range(m):
        print('{:7}'.format(a[i][j]), end='')
    print()
print()
print('Подматрица')
for i in range(len(b)):
    for j in range(len(b[0])):
        print('{:7}'.format(b[i][j]), end='')
    print()
if count > 0:
    print('\nСреднее арифметичкеское четных элементов {:<7g}'.format(summa / count))
else:
    print('\nВ подматрице нет четных элементов')
