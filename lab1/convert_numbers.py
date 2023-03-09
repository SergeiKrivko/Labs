def from_dec_to_oct(x, count=7):
    """
    Перевод числа из 10сс в 8сс с указанным кол-вом знаков после запятой
    :param x: float
    :param count: int
    :return: str
    """
    a = int(abs(x) // 1)
    b = abs(x) % 1
    res_int = ''
    res_flt = ''
    while a > 0:
        res_int = str(a % 8) + res_int
        a //= 8
    i = 0
    while b != 0 and i <= count:
        b *= 8
        res_flt += str(int(b))
        b -= b // 1
        i += 1
    if x < 0:
        res_int = '-' + res_int
    if res_flt == '':
        return res_int
    return res_int + '.' + res_flt


def from_oct_to_dec(x):
    """
    Перевод числа из 8сс в 10сс
    :param x: str
    :return: float
    """
    res = 0
    if x[0] == '-':
        x_is_negative = True
        x = x.replace('-', '')
    else:
        x_is_negative = False
    if '.' in x:
        i = x.index('.') - 1
        x = x[:x.index('.')] + x[x.index('.') + 1:]
    else:
        i = len(x) - 1
    for symbol in x:
        res += 8 ** i * int(symbol)
        i -= 1
    if x_is_negative:
        res *= -1
    return res


def number_is_oct(s):
    """
    Проверяет, является ли строка восмеричным числом
    :param s: str
    :return: bool
    """
    for el in s:
        if el not in '12345670.-':
            return False
    if s.count('.') > 1:
        return False
    if s[0] == '-':
        if s.count('-') > 1:
            return False
    elif s.count('-') > 0:
        return False
    return True
