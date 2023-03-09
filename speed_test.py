from time import time


def timeit(func):
    def timed(*args, **kwargs):
        ts = time()
        result = func(*args, **kwargs)
        te = time()
        print('func:%r took: %2.4f sec' % (func.__name__, te - ts))
        return result

    return timed

