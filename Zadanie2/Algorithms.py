import numpy as np

def solve(A, b, n):
    if niezbieznosc(A) | redukowalnosc(A):
        return [0]
    # M = findM(findN(A), findL(A), findU(A))
    M = findM(A, findN(A))
    coef = findCoef(findN(findD(A)), b)
    res0 = zero(b, 1)
    res = zero(b, 1)
    for _ in range(n):
        for i in range(len(coef)):
            res[i] += coef[i]
            for j in range(len(M)):
                res[i] += M[i][j] * res0[j]
        for i in range(len(res)):
            res0[i] = res[i]
        res = zero(b, 1)
    return res0

def niezbieznosc(A):
    res = 0
    for i in range(len(A)):
        sum = 0
        for j in range(len(A)):
            sum += A[i][j]
        if sum - A[i][i] >= A[i][i]:
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
    res = []
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            res.append(0)
        else:
            res.append(1 / matrix[i][i])
    return res

# def findM(N, L, U):
def findM(A, N):
    M = zero(A, 2)
    for i in range(len(A)):
        for j in range(len(A)):
            # L[i][j] += U[i][j]
            # L[i][j] = L[i][j] * N[i] * (-1)
            # if L[i][j] == -0.0:
            #     L[i][j] = 0
            # if i == j:
            #     L[i][j] = 0
            if i == j:
                M[i][j] = 0
            else:
                M[i][j] = - (A[i][j] * N[i])
    return M

def findCoef(N, b):
    for i in range(len(b)):
        b[i] *= N[i]
    return b