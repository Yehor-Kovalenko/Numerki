import math

from Algorithms import bisekcja, plot_function


def wielomian(x):
    return x * x - 3 * x + 2


def trygonometryczna(x):
    return math.cos(x + math.pi / 4)


def wykladnicza(x):
    return 3 ** x - 5


def zlozenie(x):
    return wielomian(x) + trygonometryczna(x) + wykladnicza(x)


print(bisekcja(trygonometryczna, 0, 2, iteracji=20))

plot_function(wykladnicza, -5, 5, bisekcja(wykladnicza, -5, 5, iteracji=30))
