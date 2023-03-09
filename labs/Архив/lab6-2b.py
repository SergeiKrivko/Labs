#   Кривко Сергей ИУ7-14Б
# 2b: Удалить элемент с заданным индексом алгоритмически.

# Ввод списка
while True:
    n = int(input('Введите длину списка: '))
    if n > 0:
        break
    print('Длина списка должна быть положительной')
a = [0]*n
for i in range(n):
    a[i] = int(input('Введите {0}-й элемент списка: '.format(i + 1)))

while True:
    index = int(input('Введите индекс: ')) - 1
    if 0 <= index < n:
        break
    print('Индекс должен быть целым числом 1 до {0}'.format(n))

for i in range(index, n - 1):           # Сдвигаем элементы вправо
    a[i] = a[i + 1]
a.pop()                                 # Удаляем последний элемент

# Вывод списка
for i in range(n - 1):
    print('a[{0}] = {1}'.format(i + 1, a[i]))
