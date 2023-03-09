from autotest import autotest
from math import gcd
import random


def bottle_count_while(money):
    count = 0
    while money >= 45:
        money -= 45
        money += 20
        count += 1
    return count


def bottle_count(money):
    return max(0, (money - 20)) // 25


def python_gcd(tpl):
    return gcd(*tpl)


def custom_gcd(tpl):
    a, b = tpl
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b


autotest(python_gcd, custom_gcd, lambda: (random.randint(0, 10000), random.randint(0, 10000)), test_count=1000000)
