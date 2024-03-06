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


# menu

print("Wybierz funkcje:\n"
      "1. trygonometryczna - cos(x + PI/4) \n"
      "2. wielomian - x^2 - 3x + 2\n"
      "3. wykladnicza - 3^x - 5\n"
      "4. zlozenie cos(x + PI/4) + x^2 - 3x + 3^x - 3")
funk = int(input())

print("Wybierz przedzial:")
print("a:")
a = int(input())
print("b:")
b = int(input())

print("Ograniczamy iloscia iteracji czy epsilonem?:\n"
      "1. iteracje\n"
      "2. epsilon")
wyb = int(input())
if wyb == 1:
    print("Wprowadz ilosc iteracji?:")
    iter = int(input())
    eps = None
elif wyb == 2:
    print("Wprowadz epsilon:")
    eps = float(input())
    iter = None

if funk == 1:
    print('bisekcja: ' + str(bisekcja(trygonometryczna, a, b, iteracji=iter, epsilon=eps)))
    plot_function(trygonometryczna, a, b, bisekcja(trygonometryczna, a, b, iteracji=iter, epsilon=eps))
    print('sieczne: ' + str(sieczne(trygonometryczna, a, b, iteracji=iter, epsilon=eps)))
    plot_function(trygonometryczna, a, b, sieczne(trygonometryczna, a, b, iteracji=iter, epsilon=eps))
elif funk == 2:
    print('bisekcja: ' + str(bisekcja(wielomian, a, b, iteracji=iter, epsilon=eps)))
    plot_function(wielomian, a, b, bisekcja(wielomian, a, b, iteracji=iter, epsilon=eps))
    print('sieczne: ' + str(sieczne(wielomian, a, b, iteracji=iter, epsilon=eps)))
    plot_function(wielomian, a, b, sieczne(wielomian, a, b, iteracji=iter, epsilon=eps))
elif funk == 3:
    print('bisekcja: ' + str(bisekcja(wykladnicza, a, b, iteracji=iter, epsilon=eps)))
    plot_function(wykladnicza, a, b, bisekcja(wykladnicza, a, b, iteracji=iter, epsilon=eps))
    print('sieczne: ' + str(sieczne(wykladnicza, a, b, iteracji=iter, epsilon=eps)))
    plot_function(wykladnicza, a, b, sieczne(wykladnicza, a, b, iteracji=iter, epsilon=eps))
elif funk == 4:
    print('bisekcja: ' + str(bisekcja(zlozenie, a, b, iteracji=iter, epsilon=eps)))
    plot_function(zlozenie, a, b, bisekcja(zlozenie, a, b, iteracji=iter, epsilon=eps))
    print('sieczne: ' + str(sieczne(zlozenie, a, b, iteracji=iter, epsilon=eps)))
    plot_function(zlozenie, a, b, sieczne(zlozenie, a, b, iteracji=iter, epsilon=eps))
