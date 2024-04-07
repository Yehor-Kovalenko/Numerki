import math

from numpy import double

A = [[0.5, -0.0625, 0.1875, 0.0625], [-0.0625, 0.5, 0, 0], [0.1875, 0, 0.375, 0.125], [0.0625, 0, 0.125, 0.25]]
# A = [[3, 3, 1], [2, 5, 7], [1, 2, 1]]
# A = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
# A = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]

b = [1.5, -1.625, 1, 0.4375]
# b = [12, 33, 8]
# b = [3, 7, 5]

from Algorithms import solve

res = solve(A, b, None, 0.1)
if res == [0]:
        print("Macierz nie spelnia warunkow zbieznosci")
else:
        for i in range(len(res)):
                print(str(res[i]))