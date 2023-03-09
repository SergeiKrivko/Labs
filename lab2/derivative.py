def split_by_pluses_and_minuses(s):
    lst = []
    level = 0
    j = -1
    for i in range(len(s)):
        if s[i] == '+' and level == 0:
            lst.append(s[j + 1:i])
            j = i
        if s[i] == '-' and level == 0:
            lst.append(s[j + 1:i])
            j = i - 1
        elif s[i] == '(':
            level += 1
        elif s[i] == ')':
            level -= 1
    lst.append(s[j + 1:])
    while '' in lst:
        lst.remove('')
    return lst


def split(s, symbol):
    level = 0
    for i in range(len(s)):
        if s[i] == symbol and level == 0:
            return s[:i], s[i + 1:]
        elif s[i] == '(':
            level += 1
        elif s[i] == ')':
            level -= 1
    return s,


std_der = [('m.sin', 'm.cos({})'),
           ('m.cos', '(-m.sin({}))'),
           ('m.tan', '1/(m.cos({})^2)'),
           ('m.sqrt', '1/2/m.sqrt({})'),
           ('m.asin', '1/m.sqrt(1-{}^2)'),
           ('m.acos', '-1/m.sqrt(1-{}^2'),
           ('m.atan', '1/(1+{}^2)'),
           ('m.log', '1/{}'),
           ('m.log10', '1/{}*m.log(10)'),
           ('m.log2', '1/{}*m.log(2)'),
           ('m.exp', 'm.exp({})')]


def derivative(func, var='x'):
    func = func.replace(' ', '')
    func = func.replace('**', '^')
    func = func.replace('math', 'm')
    try:
        float(func)
        return '0'
    except Exception:
        pass
    if func == var:
        return '1'

    if func == '-' + var:
        return '-1'

    tpl1 = split_by_pluses_and_minuses(func)
    if len(tpl1) > 1:
        return '(' + '+'.join((map(derivative, tpl1))) + ')'

    tpl2 = split(tpl1[0], '*')
    if len(tpl2) == 2:
        return '(' + derivative(tpl2[0]) + '*' + tpl2[1] + '+' + tpl2[0] + '*' + derivative(tpl2[1]) + ')'

    tpl3 = split(tpl2[0], '/')
    if len(tpl3) == 2:
        return '(' + derivative(tpl3[0]) + '*' + tpl3[1] + '-' + tpl3[0] + '*' + derivative(tpl3[1]) + ')/(' \
               + tpl3[1] + '^2)'

    tpl4 = split(tpl3[0], '^')
    if len(tpl4) == 2:
        return tpl4[1] + '*' + tpl4[0] + '^' + str(float(tpl4[1]) - 1) + '*' + derivative(tpl4[0])

    for f, d in std_der:
        if tpl4[0][:len(f)] == f and tpl4[0][len(f)] == '(' and tpl4[0][-1] == ')':
            return d.format(tpl4[0][len(f):]) + '*' + derivative(tpl4[0][len(f) + 1:-1])

    for f, d in std_der:
        if tpl4[0][:len(f) + 1] == '-' + f and tpl4[0][len(f) + 1] == '(' and tpl4[0][-1] == ')':
            return '-' + d.format(tpl4[0][len(f) + 1:]) + '*' + derivative(tpl4[0][len(f) + 2:-1])

    if func[0] == '(' and func[-1] == ')':
        return derivative(func[1:-1], var)

    print('ERROR', func)


def der(func, var='x'):
    return derivative(func, var).replace('^', '**')


def main():
    print(derivative(derivative('m.sin(m.cos(-x - 18) ** 2)')))


if __name__ == '__main__':
    main()
