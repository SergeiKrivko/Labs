from lab2.derivative import der


class MathFunction:
    def __init__(self, func, var='x'):
        self.func_str = func
        self.var = var
        self.func_lambda = eval(f'lambda {var}:{func}')

    def __call__(self, *args, **kwargs):
        return self.func_lambda(*args, **kwargs)

    def deriv(self):
        return MathFunction(der(self.func_str), var=self.var)

    def __str__(self):
        return self.func_str

