import math

from Algorithms import bisekcja


def wielomian(x):
    return x * x - 3 * x + 2


def trygonometryczna(x):
    return math.cos(x + math.pi / 4)


def wykladnicza(x):
    return 3 ** x - 2

def zlozenie(x):
    return wielomian(x) + trygonometryczna(x) + wykladnicza(x)


print(bisekcja(wielomian, 1, 5, iteracji=20))
