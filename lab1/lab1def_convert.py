def covert_to_reverse_code(x):
    """
    Перевод двоичного числа в обратный код
    :param x: str
    :return: str
    """
    if x[0] == '0':
        return x

    res = ['1']
    for i in range(1, 8):
        if x[i] == '1':
            res.append('0')
        elif x[i] == '0':
            res.append('1')
        else:
            raise ValueError
    return ''.join(res)


def convert_to_added_code(r):
    """
    Перевод двоичного числа в дополнительный код
    :param r: str
    :return: str
    """
    if r[0] == '0':
        return r

    lst = list(r)
    for i in range(7, 0, -1):
        if lst[i] == '1':
            lst[i] = '0'
        elif lst[i] == '0':
            lst[i] = '1'
            break
    else:
        return 'Переполнение'
    return ''.join(lst)
