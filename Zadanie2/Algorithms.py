import copy

import numpy as np
from itertools import *

def solve(data, n=None, epsilon=None):
    perm = zbieznosc(data)
    if perm.any() == None:
        return None
    A = getA(perm)
    b = getB(perm)
    M = findM(A, findN(A))
    coef = findCoef(findN(findD(A)), b)
    res0 = zero(b, 1)
    res = zero(b, 1)
    if n is not None:
        for _ in range(n):
            oblicz(res0, res, M, coef)
            for i in range(len(res)):
                res0[i] = res[i]
            res = zero(b, 1)
        return res0
    else:
        while True:
            oblicz(res0, res, M, coef)
            tmp = 0
            for i in range(len(res)):
                if abs(res0[i] - res[i]) < epsilon:
                    tmp += 1
            if tmp == len(res):
                return res
            for i in range(len(res)):
                res0[i] = res[i]
            res = zero(b, 1)

def zbieznosc(data):
    A = getA(data)
    if dominacja(A):
        change(data, A)
    if dominacja(A) | redukowalnosc(A):
        return None
    return data

def swap(arr, x, y):
    t = [copy.deepcopy(arr[x]), copy.deepcopy(arr[y])]
    arr[x] = t[1]
    arr[y] = t[0]

def change(data, A):
    for i in range(len(data)):
        swap(data, i, A[i].index(max(A[i])))
        swap(A, i, A[i].index(max(A[i])))

def oblicz(res0, res, M, coef):
    for i in range(len(coef)):
        res[i] += coef[i]
        for j in range(len(M)):
            res[i] += M[i][j] * res0[j]
    return res

def getA(data):
    A = []
    size = len(data)
    for i in range(size):
        A.append([])
        for j in range(size):
            A[i].append(data[i][j])
    return A

def getB(data):
    b = []
    size = len(data)
    for i in range(size):
        b.append(data[i][size])
    return b

def dominacja(A):
    res = 0
    for i in range(len(A)):
        sum = 0
        for j in range(len(A)):
            if i != j:
                sum += A[j][i]
        if abs(sum) >= abs(A[i][i]):
            res += 1
    if res == 0:
        return False
    else:
        return True

def redukowalnosc(A):
    boolean = True
    tmp_row = np.zeros(len(A))
    tmp_col = np.zeros(len(A))
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] != 0:
                tmp_row[j] += 1
            if A[j][i] != 0:
                tmp_col[j] += 1
    for k in range(len(A)):
        if tmp_row[k] != 1:
            boolean = False
    if boolean:
        return boolean
    boolean = True
    for k in range(len(A)):
        if tmp_col[k] != 1:
            boolean = False
    return boolean


def zero(matrix, d):
    zero = []
    for i in range(len(matrix)):
        if d == 2:
            zero.append([])
            for j in range(len(matrix)):
                zero[i].append(0)
        else:
            zero.append(0)
    return zero

def findD(matrix):
    res = zero(matrix, 2)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j == i:
                res[i][j] = matrix[i][j]
    return res

def findN(matrix):
    res = []
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            res.append(0)
        else:
            res.append(1 / matrix[i][i])
    return res

def findM(A, N):
    M = zero(A, 2)
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                M[i][j] = 0
            else:
                M[i][j] = - (A[i][j] * N[i])
    return M

def findCoef(N, b):
    for i in range(len(b)):
        b[i] *= N[i]
    return b