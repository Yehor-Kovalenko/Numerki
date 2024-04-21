import matplotlib.pyplot as plt
import numpy as np

def czebyszew(a, b, n):
    x = []
    for i in range(n):
        x.append((a + b) / 2 + (b - a) * np.cos(np.pi * (2 * i + 1) / (2 * n + 2)) / 2)
    return x

def wezly(f, x):
    y = []
    for i in range(len(x)):
        y.append(f(x[i]))
    return y

def wspolczynniki(x, y):
    coef = []
    for i in range(len(y)):
        coef.append(y[i])
        for j in range(len(x)):
            if x[i] != x[j]:
                coef[i] = coef[i] / (x[i] - x[j])
    return coef

def lagrange(coef, _x, x):
    res = []
    for i in range(len(coef)):
        res.append(coef[i])
        for j in range(len(_x)):
            if i != j:
                res[i] = res[i] * (x - _x[j])
    result = 0
    for i in range(len(res)):
        result += res[i]
    return result

def interpolacja(f, a, b, n):
    x = czebyszew(a, b, n)
    y = wezly(f, x)
    coef = wspolczynniki(x, y)
    plot_function(f, a, b, coef, x)

def plot_function(f, a, b, coef, X):
    x = np.linspace(a, b, 50)
    plt.axvline(x=0, color="black", linewidth=0.5)
    plt.axhline(y=0, color="black", linewidth=0.5)
    fv = np.vectorize(f)
    plt.plot(x, fv(x), label= 'Funkcja')
    plt.plot(x, lagrange(coef, X, x), label='Interpolacja')
    plt.plot(X, lagrange(coef, X, X), '+', markersize=12, color="red", label='Węzły')
    plt.legend()
    plt.show()