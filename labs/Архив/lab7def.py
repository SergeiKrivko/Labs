#   Кривко Сергей ИУ7-14Б
# Удаление всех неуникальных элементов из списка.

# Ввод списка
while True:
    n = int(input('Введите длину списка: '))
    if n > 0:
        break
    print('Длина списка должна быть натуральным числом')
a = []
for i in range(n):
    a.append(int(input('Введите {0}-й элемент списка: '.format(i + 1))))


i = 0
j = 0

while j < n:
    for k in range(i):
        if a[k] == a[j]:
            j += 1
            break
    else:
        a[i] = a[j]
        i += 1
        j += 1

a = a[:i]


# Вывод списка
for i in range(i):
    print('a[{0}] = {1}'.format(i + 1, a[i]))
