__all__ = ['my_sum', 'factorial', 'sin']

from functools import cache


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return n * factorial(n-1) if n else 1


@cache
def sin(x):
    y = 0
    for n in range(100):
        y = y + ((-1)**n * (x)**(2*n+1)) / factorial(2*n+1)
    return y
