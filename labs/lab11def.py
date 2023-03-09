def binary_search_insertion(array):
    for i in range(1, len(array)):
        x = array[i]
        if array[i] < a[i - 1]:
            left = 0
            right = i - 1
            while left < right:
                center = (left + right) // 2
                if x < a[center]:
                    right = center
                else:
                    left = center + 1
            for j in range(i, right, -1):
                array[j] = array[j - 1]
            array[right] = x


n = int(input('Введите длину массива: '))
a = []
for i in range(n):
    a.append(int(input('Введите {0}-й элемент массива: '.format(i + 1))))

binary_search_insertion(a)

print('\nОтсортированный массив: ')
for i in range(n):
    print('{0:<6}'.format(a[i]), end=' ')
print()
