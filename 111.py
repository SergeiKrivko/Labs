def integral(function, start, stop, step):
    res = 0
    x = start
    while x < stop + step // 2:
        res += function(x)
        x += step
    return res * step


def f(x):
    return x ** 2

