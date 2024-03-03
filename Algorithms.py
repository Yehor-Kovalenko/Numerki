def bisekcja(f, a, b, iteracji=None, epsilon=None):
    # jesli f(a)*f(b) jest wieksze od 0 to rzucic wyjatek bo funkcja nie zmienia znaku
    if f(a) * f(b) > 0:
        raise ValueError("Error, f(", a, ") * f(", b, ") >= 0. f(a)*f(b) must be less than zero!\n")
    x = 0
    k = 0

    # jesli iteracji zostaly podany jako warunek stopu
    if iteracji is not None:
        c = 0
        while k < iteracji:  # wykonywac dopoty, dopoki warunek stopu nie zostanie osiagniety
            c = (a + b) / 2
            if f(c) == 0:
                return c
            elif f(a)*f(c) < 0:
                b = c
            elif f(c)*f(b) < 0:
                a = c
            k += 1
        return c

    # jesli dokladnosc zostala podana jako warunek stopu
    else:
        print("what")
        return x


def sieczne(a, b, iteracji=None, dokladnosc=None):
    x = 0
    k = 0
    if iteracji is not None:
        while k < iteracji:
            print("hello")
            k += 1
        return x
    else:
        print("what")
        return x
