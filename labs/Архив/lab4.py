#   Кривко Сергей ИУ7-14Б
#Построение таблицы значений двух функций и графика одной из них

import math as m

#Ввод данных
while True:
    start = float(input('Введите начальное значение аргумента: '))
    stop = float(input('Введите конечное значение аргумента: '))
    step = float(input('Введите шаг: '))
    while step == 0:
        print('Шаг не может быть равен 0')
        step = float(input('Введите шаг: '))
    if (stop - start) * step > 0:
        break
    print('Введенные значения некорректны.')


#Печать шапки таблицы
print('-'*52)
print('|       x        |       Z        |       Q        |')
print('|', '-'*50, '|', sep='')
a = start
Z_min = 4.81*a**3 + 2.44*a**2 - 14.78*a - 5.99      #Минимальное значение функции Z
Q_min = Q_max = 6.31*a**2 - 8.24*a*m.pi - 2         #Минимальное и максимальное значение функции Q
for i in range(int((stop - start) / step + 1)):  #Проходим циклом по всем значениям аргумента
    Z = 4.81*a**3 + 2.44*a**2 - 14.78*a - 5.99      #Для каждого значения х находим значения Z и Q
    Q = 6.31*a**2 - 8.24*a*m.pi - 2
    print('|  {0:12.6g}  |  {1:12.6g}  |  {2:12.6g}  |'.format(round(a,1), Z, Q))      #Печатаем строку таблицы
    Z_min = min(Z_min, Z)
    Q_min = min(Q_min, Q)
    Q_max = max(Q_max, Q)
    a += step
print('-'*49)

#Построение графика функции Q
while True:
    count = int(input('Введите количество засечек (от 4 до 8): '))      #Ввод количества засечек
    if 4 <= count <= 8:
        break

step_Q = (Q_max - Q_min) / (count - 1)        #Находим шаг между засечками по оси Q
print('            | ', end = '')

k = Q_min
for i in range(count):      #Печатаем засечки на оси Q
    if 80 % count > i:
        print('{:10.5g}'.format(k), ' '*(80 // count - 8), sep = '', end = '')
    else:
        print('{:10.5g}'.format(k), ' '*(80 // count - 9), sep = '', end = '')
    k += step_Q
print()

a = start
step_Q = (Q_max - Q_min) / 79          #Находим шаг по оси Q, 80 - ширина в символах оновной части графика
for i in range(int((stop - start) / step + 1)):      #Проходим циклом по всем значениям аргумента
    Q = 6.31*a**2 - 8.24*a*m.pi - 2                     #Для каждого считаем значение Q
    print('{0:11.6g} |       '.format(round(a,1)), end = '')        #Печатаем значение аргумента
    k = Q_min
    for j in range(80):                         #Проходим циклом по всем 80 позициям по оси Q
        if abs(k - Q) < step_Q / 2:             #Если значение функции попадает на данную позицию, печатаем '*'
            print('*', end = '')
        elif abs(k) < step_Q / 2:               #Если на данную позицию попадает 0, печатаем символ '|'
            print('|', end = '')
        else:                                   #Иначе печатаем пробел
            print(' ', end='')
        k += step_Q
    a += step
    print()
print()

#Дополнительное задание. Z_min + Q_min
summ = Z_min + Q_min
print('Z_min + Q_min = {:<7g}'.format(summ))