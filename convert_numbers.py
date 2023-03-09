def from_10_to_n(a, n, count=10):
    alph = '0123456789abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    a, b = int(a), a - int(a)
    a_n = ''
    b_n = ''
    while a > 0:
        a_n = alph[a % n] + a_n
        a //= n
    i = 0
    while b != 0 and i <= count:
        b *= n
        b_n += alph[int(b)]
        b -= int(b)
        i += 1
    return a_n + '.' + b_n


def from_n_to_10(a, n):
    pass


for n in range(2, 70):
    print(n, ':', from_10_to_n(123456789.987654321, n, 100))
