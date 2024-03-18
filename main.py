import math

from Algorithms import bisekcja, plot_function, sieczne

#coefficients for the horner scheme starting from the highest power of the x
coef = [1, -3, 2]
#x^2 -3x + 2


def wielomian(x):
    res = 0
    for i in coef:
        res = res * x + i
    return res


def trygonometryczna(x):
    return math.cos(x)


def wykladnicza(x):
    return 3 ** x - 5


def zlozenie(x):
    return trygonometryczna(wielomian(wykladnicza(x)))

def print_plot(f, a, b, iter, eps):
    bisekcja_ans, iteracji = bisekcja(f, a, b, iteracji=iter, epsilon=eps)
    print('bisekcja: ' + str(bisekcja_ans))
    print("Number of completed iterations: " + str(iteracji))
    plot_function(f, a, b, bisekcja_ans, title="Bisekcja")

    sieczne_ans, iteracji = sieczne(f, a, b, iteracji=iter, epsilon=eps)
    print('sieczne: ' + str(sieczne_ans))
    print("Number of completed iterations: " + str(iteracji))
    plot_function(f, a, b, sieczne_ans, title="Metoda siecznych")


# menu

print("Wybierz funkcje:\n"
      "1. trygonometryczna - cos(x + PI/4) \n"
      "2. wielomian - x^2 - 3x + 2\n"
      "3. wykladnicza - 3^x - 5\n"
      "4. zlozenie cos(x + PI/4)○(x^2 - 3x+2)○(3^x - 5)")
funk = int(input())

print("Wybierz przedzial:")
print("a:")
a = float(input())
print("b:")
b = (float(input()))

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
    print_plot(trygonometryczna, a, b, iter, eps)
elif funk == 2:
    print_plot(wielomian, a, b, iter, eps)
elif funk == 3:
    print_plot(wykladnicza, a, b, iter, eps)
elif funk == 4:
    print_plot(zlozenie, a, b, iter, eps)
