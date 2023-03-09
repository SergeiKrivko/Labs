import math


def convert_bin_to_gray_code(x):
    """Преобразование двоичного числа в код Грея"""
    code = x[2]
    for i in range(3, len(x)):
        if x[i] != x[i - 1]:
            code += '1'
        else:
            code += '0'
    return code


def convert_table_to_formula(table):
    """Восстановление формулы по таблице истинности"""
    def k(x):
        if x % 2:
            return -1
        return 1

    variables = int(math.log2(len(table)))

    for i in range(len(table)):
        if table[i]:
            a = []
            flag = True
            for j in range(1, len(table)):
                for l in range(variables):
                    if table[i + k(i) * j % l // 2] == 0:
                        flag = False
                        break
                if not flag:
                    break
            else:
                pass



print(convert_table_to_formula([0, 0, 0, 1, 0, 1, 1, 1]))
