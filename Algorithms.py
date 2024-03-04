import numpy as np
from matplotlib import pyplot as plt


def bisekcja(f, a, b, iteracji=None, epsilon=None):
    # sprawdzenie koncow przedzialu
    if f(a) == 0:
        return a
    elif f(b) == 0:
        return b

    # jesli f(a)*f(b) > 0 to rzucic wyjatek bo funkcja nie zmienia znaku
    if f(a) * f(b) > 0:
        raise ValueError("Error, f(", a, ") * f(", b, ") >= 0. f(a)*f(b) must be less than zero!\n")

    c = 0

    # jesli iteracji zostaly podany jako warunek stopu
    if iteracji is not None:
        k = 0
        while k < iteracji:  # wykonywac dopoty, dopoki warunek stopu nie zostanie osiagniety
            c = (a + b) / 2
            if f(c) == 0:
                return c
            elif f(a) * f(c) < 0:
                b = c
            elif f(c) * f(b) < 0:
                a = c
            k += 1

    # jesli dokladnosc zostala podana jako warunek stopu
    else:
        # poki dokladnosc nie zostala osiagnieta
        while (a - b) < epsilon:
            c = (a + b) / 2
            if f(c) == 0:
                return c
            elif f(a) * f(c) < 0:
                b = c
            elif f(c) * f(b) < 0:
                a = c
    return c


def sieczne(f, a, b, iteracji=None, dokladnosc=None):
    k = 0
    xn = b # X n
    xn1 = 0 # X n+1
    xn_1 = a # X n-1
    if iteracji is not None:
        while k < iteracji:
            if xn == xn_1:
                break
            xn1 = xn - (f(xn) * (xn-xn_1)) / (f(xn) - f(xn_1))
            k += 1
            xn_1 = xn
            xn = xn1
        return xn
    else:
        while (a - b) < dokladnosc:
            if xn == xn_1:
                break
            xn1 = xn - (f(xn) * (xn-xn_1)) / (f(xn) - f(xn_1))
            k += 1
            xn_1 = xn
            xn = xn1
        return xn


def plot_function(f, a, b, x0):
    x = np.linspace(a, b, 50)
    plt.axvline(x=0, color="black", linewidth=0.5)
    plt.axhline(y=0, color="black", linewidth=0.5)
    fv = np.vectorize(f)
    plt.plot(x, fv(x), label= 'Funkcja')
    plt.plot(x0, f(x0), '+', markersize=12, color="red", label='Miejsce zerowe')
    plt.legend()
    plt.show()
