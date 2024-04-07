import csv
import numpy as np
from Algorithms import solve

data = open("data/data44.csv")
csv.reader(data)
rows = []
for row in csv.reader(data):
        rows.append(row)
data = np.array(rows, dtype=np.float64)

if len(data[0]) != len(data) + 1:
        print("Nieprawidlowy rozmiar macierzy!")
else:
        A = []
        b = []

        size = len(data)

        for i in range(size):
                A.append([])
                for j in range(size):
                        A[i].append(data[i][j])
                b.append(data[i][size])

        res = solve(A, b, 20)
        if res == [0]:
                print("Macierz nie spelnia warunkow zbieznosci")
        else:
                for i in range(len(res)):
                        print(str(res[i]))