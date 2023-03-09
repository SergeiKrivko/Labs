#   Кривко Сергей ИУ7-14Б
# Нахождение самой длинной последовательности нулевых элементов

while True:
    n = int(input('Введите длину списка: '))
    if n > 0:
        break
    print('Длина должна быть положительным числом')
a = []
for i in range(n):
    a.append(int(input('Введите {0}-й элемент: '.format(i + 1))))

current_len = 0
max_len = 0
end = 0

for i in range(n):
    if a[i] == 0:
        current_len += 1
    else:
        if current_len > max_len:
            max_len = current_len
            end = i - 1
        current_len = 0
if current_len > max_len:
    max_len = current_len
    end = n

if max_len > 0:
    print('Максимальная длина последовательности нулевых элементов: {0} (с {1}-го по {2}-й элементы)'.format(max_len,
                                                                                end - max_len + 2, end + 1))
    print('0, ' * max_len, '\b\b\b')
else:
    print('В списке нет нулевых элементов')
