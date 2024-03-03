from Algorithms import bisekcja


def sqr(x):
    return x * x


print(bisekcja(sqr, -1, 1, iteracji=40))
