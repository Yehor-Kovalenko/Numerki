import numpy as np

def solve(A, b, n):
    M = findM(findN(findD(A)), findL(A), findU(A))
    coef = findCoef(findN(findD(A)), b)
    res0 = zero(b, 1)
    res = zero(b, 1)
    for _ in range(n):
        for i in range(len(coef)):
            res[i] += coef[i]
            for j in range(len(M)):
                res[i] += (M[i][j] * res0[j])
        for i in range(len(res)):
            res0[i] = res[i]
        res = zero(b, 1)
    return res0

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

def findL(matrix):
    res = zero(matrix, 2)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j < i:
                res[i][j] = matrix[i][j]
    return res

def findU(matrix):
    res = zero(matrix, 2)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j > i:
                res[i][j] = matrix[i][j]
    return res

def findD(matrix):
    res = zero(matrix, 2)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j == i:
                res[i][j] = matrix[i][j]
    return res

def findN(matrix):
    res = matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j == i:
                res[i][j] = 1 / matrix[i][j]
    return res

def findM(N, L, U):
    for i in range(len(L)):
        for j in range(len(L)):
            L[i][j] += U[i][j]
            L[i][j] = L[i][j] * N[i][i] * (-1)
            if L[i][j] == -0.0:
                L[i][j] = 0
    return L

def findCoef(N, b):
    for i in range(len(b)):
        b[i] *= N[i][i]
    return b