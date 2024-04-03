import math

from numpy import double

A = [[0.5, -0.0625, 0.1875, 0.0625], [-0.0625, 0.5, 0, 0], [0.1875, 0, 0.375, 0.125], [0.0625, 0, 0.125, 0.25]]
#A = [[3, 3, 1], [2, 5, 7], [1, 2, 1]]

b = [1.5, -1.625, 1, 0.4375]
#b = [12, 33, 8]

from Algorithms import solve

res = solve(A, b, 20)
for i in range(len(res)):
        print(str(res[i]))