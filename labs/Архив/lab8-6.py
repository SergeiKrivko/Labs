#   Кривко Сергей ИУ7-14Б
# 6: Транспонирование квадратной матрицы.


# Ввод матрицы
while True:
    n = int(input('Введите размер квадратной матрицы: '))
    if n > 0:
        break
    print('Размер должен быть положительным')
a = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input('Введите {0}-й элемент {1}-ой строки матрицы: '.format(i + 1, j + 1)))


for i in range(n):                      # Проходим по всем элементам матрицы над главной диагональю
    for j in range(i + 1, n):
        a[i][j], a[j][i] = a[j][i], a[i][j]     # Меняем их местами с симметричным относительно диагонали


# Вывод матрицы
print()
for i in range(n):
    for j in range(n):
        print('{0:6} '.format(a[i][j]), end='')
    print()
