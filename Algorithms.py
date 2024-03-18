import numpy as np
from matplotlib import pyplot as plt


def bisekcja(f, a, b, iteracji=None, epsilon=None):
    # sprawdzenie koncow przedzialu
    if f(a) == 0:
        return a
    elif f(b) == 0:
        return b

    # jesli f(a)*f(b) > 0 to rzucic wyjatek bo funkcja nie zmienia znaku

    c = 0
    number_of_iterations = 0
    # jesli iteracji zostaly podany jako warunek stopu
    if iteracji is not None:
        k = 0
        while k < iteracji:  # wykonywac dopoty, dopoki warunek stopu nie zostanie osiagniety
            c = (a + b) / 2
            number_of_iterations += 1
            if f(c) == 0:
                print("Number of completed iterations: " + str(number_of_iterations))
                return c
            elif f(a) * f(c) < 0:
                b = c
            elif f(c) * f(b) < 0:
                a = c
            k += 1

    # jesli dokladnosc zostala podana jako warunek stopu
    else:
        # poki dokladnosc nie zostala osiagnieta
        while abs(a - b) >= epsilon:
            c = (a + b) / 2
            number_of_iterations += 1
            if f(c) == 0:
                print("Number of completed iterations: " + str(number_of_iterations))
                return c
            elif f(a) * f(c) < 0:
                b = c
            elif f(c) * f(b) < 0:
                a = c
    print("Number of completed iterations: " + str(number_of_iterations))
    return c


def sieczne(f, a, b, iteracji=None, epsilon=None):
    number_of_iterations = 0
    k = 0
    xn = b # X n
    xn1 = 0 # X n+1
    xn_1 = a # X n-1
    if iteracji is not None:
        while k < iteracji:
            if xn == xn_1:
                break
            number_of_iterations += 1
            xn1 = xn - (f(xn) * (xn-xn_1)) / (f(xn) - f(xn_1))
            k += 1
            xn_1 = xn
            xn = xn1
        print("Number of completed iterations: " + str(number_of_iterations))
        return xn
    else:
        while abs(xn - xn_1) >= epsilon:
            if xn == xn_1:
                break
            number_of_iterations += 1
            xn1 = xn - (f(xn) * (xn-xn_1)) / (f(xn) - f(xn_1))
            k += 1
            xn_1 = xn
            xn = xn1
        print("Number of completed iterations: " + str(number_of_iterations))
        return xn
