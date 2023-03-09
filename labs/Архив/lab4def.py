#   Кривко Сергей ИУ7-14Б

start = float(input('Введите начальное значение аргумента: '))
stop = float(input('Введите конечное значение аргумента: '))
step = float(input('Введите шаг значение аргумента: '))

y_min = 4 - max(start ** 2, stop ** 2)
if min(start, stop) < 0 < max(start, stop):
    y_max = 4
else:
    y_max = 4 - min(start ** 2, stop ** 2)

print('            | {:<7g}'.format(y_min), ' '*64, '{:7g}'.format(y_max))
step_y = (y_max - y_min) / 79
x = start
for i in range(int((stop - start) / step + 1)):
    y = 4 - x ** 2
    print('{:11.6g} | '.format(round(x, 10)), end = '')
    t = y_min
    for j in range(80):
        if abs(t - y) < step_y / 2:
            print('*', end = '')
        elif abs(t) < step_y / 2:
            print('|', end = '')
        else:
            print(' ', end = '')
        t += step_y
    print()
    x += step