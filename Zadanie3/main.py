import math

from Zadanie3.Algorithms import interpolacja

#coefficients for the horner scheme starting from the highest power of the x
coef = [1, -3, 2]
#x^2 -3x + 2

def liniowa(x):
    return 2 * x + 5

def wielomian(x):
    res = 0
    for i in coef:
        res = res * x + i
    return res

def trygonometryczna(x):
    return math.cos(x + math.pi/4)

def absolute(x):
    return abs(x)

def zlozenie(x):
    return trygonometryczna(wielomian(absolute(liniowa(x))))

# menu

print("Wybierz funkcje:\n"
      "1. trygonometryczna\n"
      "2. wielomian\n"
      "3. liniowa\n"
      "4. |x|\n"
      "5. zlozenie")
funk = int(input())

print("Wybierz przedzial:")
print("a:")
a = float(input())
print("b:")
b = (float(input()))

print("Wprowadz ilosc wezlow:")
n = (int(input()))

if funk == 1:
    interpolacja(trygonometryczna, a, b, n)
elif funk == 2:
    interpolacja(wielomian, a, b, n)
elif funk == 3:
    interpolacja(liniowa, a, b, n)
elif funk == 4:
    interpolacja(absolute, a, b, n)
elif funk == 5:
    interpolacja(zlozenie, a, b, n)
