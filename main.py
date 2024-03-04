import math

from Algorithms import bisekcja, plot_function, sieczne


def wielomian(x):
    return x * x - 3 * x + 2


def trygonometryczna(x):
    return math.cos(x + math.pi / 4)


def wykladnicza(x):
    return 3 ** x - 5


def zlozenie(x):
    return wielomian(x) + trygonometryczna(x) + wykladnicza(x)


print(bisekcja(trygonometryczna, 0, 2, iteracji=20))
plot_function(trygonometryczna, 0, 2, bisekcja(trygonometryczna, 0, 2, iteracji=20))


# menu

print("Wybierz metode:\n"
      "1. bisekcja\n"
      "2. sieczne")
met = int(input())

print("Wybierz funkcje:\n"
      "1. trygonometryczna\n"
      "2. wielomian\n"
      "3. wykladnicza\n"
      "4. zlozenie")
funk = int(input())

print("Wybierz przedzial:")
print("a:")
a = int(input())
print("b:")
b = int(input())

print("Wprowdz ilosc iteracji:")
iter = int(input())

if funk == 1:
    if met == 1:
        print(bisekcja(trygonometryczna, a, b, iteracji=iter))
        plot_function(trygonometryczna, a, b, bisekcja(trygonometryczna, a, b, iteracji=iter))
    elif met == 2:
        print(sieczne(trygonometryczna, a, b, iteracji=iter))
        plot_function(trygonometryczna, a, b, sieczne(trygonometryczna, a, b, iteracji=iter))
elif funk == 2:
    if met == 1:
        print(bisekcja(wielomian, a, b, iteracji=iter))
        plot_function(wielomian, a, b, bisekcja(wielomian, a, b, iteracji=iter))
    elif met == 2:
        print(sieczne(wielomian, a, b, iteracji=iter))
        plot_function(wielomian, a, b, sieczne(wielomian, a, b, iteracji=iter))
elif funk == 3:
    if met == 1:
        print(bisekcja(wykladnicza, a, b, iteracji=iter))
        plot_function(wykladnicza, a, b, bisekcja(wykladnicza, a, b, iteracji=iter))
    elif met == 2:
        print(sieczne(wykladnicza, a, b, iteracji=iter))
        plot_function(wykladnicza, a, b, sieczne(wykladnicza, a, b, iteracji=iter))
elif funk == 4:
    if met == 1:
        print(bisekcja(zlozenie, a, b, iteracji=iter))
        plot_function(zlozenie, a, b, bisekcja(zlozenie, a, b, iteracji=iter))
    elif met == 2:
        print(sieczne(zlozenie, a, b, iteracji=iter))
        plot_function(zlozenie, a, b, sieczne(zlozenie, a, b, iteracji=iter))
