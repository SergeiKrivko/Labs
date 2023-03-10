#   Кривко Сергей ИУ7-14Б
# 5: Поменять местами минимальный четный и максимальный нечетный.

# Ввод списка
while True:
    n = int(input('Введите длину списка: '))
    if n > 0:
        break
    print('Длина списка должна быть положительной')
a = [0]*n
for i in range(n):
    a[i] = int(input('Введите {0}-й элемент списка: '.format(i + 1)))

min_even = -1                     # Индекс минимального четного элемента
max_odd = -1                      # Индекс максимального нечетного элемента


for i in range(n):
    if a[i] % 2 == 0:
        if min_even == -1 or a[i] < a[min_even]:    # Элемент четный: сравниваем его с текущим максимумом
            min_even = i
    elif max_odd == -1 or a[i] > a[max_odd]:        # Элемент нечетный: сравниваем его с текущим минимумом
        max_odd = i

if min_even == -1:
    print('В массиве нет четных чисел')
elif max_odd == -1:
    print('В массиве нет нечетных чисел')
else:
    a[min_even], a[max_odd] = a[max_odd], a[min_even]   # Меняем элементы местами
    # Вывод списка
    for i in range(n):
        print('a[{0}] = {1}'.format(i + 1, a[i]))
