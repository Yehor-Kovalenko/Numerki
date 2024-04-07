import csv
import numpy as np
from Algorithms import solve

print("Ograniczamy iloscia iteracji czy epsilonem?\n"
      "1. iteracje\n"
      "2. epsilon")
wyb = int(input())
if wyb == 1:
    print("Wprowadz ilosc iteracji:")
    iter = int(input())
    eps = None
elif wyb == 2:
    print("Wprowadz epsilon:")
    eps = float(input())
    iter = None
print("Wybierz rozmiar macierzy:\n"
      "1. 3x3\n"
      "2. 4x4")
wyb = int(input())
if wyb == 1:
    print("Wprowadz numer macierzy(od 1 do 8):")
    nr = 30+ int(input())
elif wyb == 2:
    print("Wprowadz numer macierzy(od 1 do 4):")
    nr = 40 + int(input())


data = open("data/data" + str(nr) + ".csv")
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