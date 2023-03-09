#   Кривко Сергей ИУ7-14Б
# 3: Найти значение K-го экстремума в списке.

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
    K = int(input('Введите номер необходимого экстремума: '))
    if K > 0:
        break
    print('Введите положительное число')

count = 0            # Кол-во уже найденных экстремумов

for i in range(1, n - 1):                       # Проходим по всему списку
    # если текущий элемент больше(меньше) и предыдущего, и последующего,
    if (a[i - 1] < a[i] and a[i + 1] < a[i]) or (a[i - 1] > a[i] and a[i + 1] > a[i]):
        count += 1                                  # то он является экстремумом
        if count == K:                              # Если номер этого экстремума равен искомому,
            print('Значение {0}-го экстремума: a[{1}] = {2}'.format(K, i, a[i]))            # выводим его значение
            break                                                               # и прерываем цикл
else:
    print('В списке меньше {0} экстремумов'.format(K))
