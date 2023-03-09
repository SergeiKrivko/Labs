#   Кривко Сергей ИУ7-14Б
# Ввести трёхмерный массив, вывести из него i-й срез (матрицу - фрагмент трёхмерного массива) по второму индексу

# Ввод трехмерного массива
while True:
    x_size = int(input('Введите размер массива по x: '))
    if x_size > 0:
        break
    print('Размер массива должен быть натуральным числом')
while True:
    y_size = int(input('Введите размер массива по y: '))
    if y_size > 0:
        break
    print('Размер массива должен быть натуральным числом')
while True:
    z_size = int(input('Введите размер массива по z: '))
    if z_size > 0:
        break
    print('Размер массива должен быть натуральным числом')
a = []
for i in range(x_size):
    a.append([])
    for j in range(y_size):
        a[i].append([])
        for k in range(z_size):
            a[i][j].append(int(input('Введите элемент [{0}][{1}][{2}]: '.format(i + 1, j + 1, k + 1))))
# Ввод номера среза
while True:
    index = int(input('Введите номер среза: ')) - 1
    if 0 <= index < y_size:
        break
    print('Номер среза должен быть натуральным числом от 1 до {0}'.format(y_size))

# Вывод среза
print()
for i in range(x_size):
    for j in range(z_size):
        print(' {0:5} '.format(a[i][index][j]), end='')
    print()
print()
