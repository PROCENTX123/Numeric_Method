from typing import List

def lu_decomposition(A: List[List[float]]) -> [List[List[float]], List[List[float]]]:
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for k in range(i, n):
            sum_ = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_

        for k in range(i, n):
            if i == k:
                L[i][i] = 1.0
            else:
                sum_ = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - sum_) / U[i][i]

    return L, U

def matrix_multuply(L: List[List[float]], U: List[List[float]]) -> List[List[float]]:
    C = [[0.0] * len(U[0]) for _ in range(len(L))]

    for i in range(len(L)):
        for j in range(len(U[0])):
            for k in range(len(U)):
                C[i][j] += L[i][k] * U[k][j]

    return C

if __name__ == "__main__":
    A = [[2, -1, 1],
         [-3, -1, 4],
         [-1, 1, 3]]

    L, U = lu_decomposition(A)

    print("LU разложение")

    print("Матрица L")
    for row in L:
        print(row)

    print("Матрица U")
    for row in U:
        print(row)

    print()
    print()

    print("Проверка того что произведение возвращает исходную матрицу")
    A1 = matrix_multuply(L, U)

    print("Исходная матрица")
    for row in A:
        print(row)

    print("Произведение L U")
    for row in A1:
        print(row)

    print("Погрешность")
    norm_error = max(abs(A[i][j] - A1[i][j]) for i in range(len(A)) for j in range(len(A[0])))
    print(norm_error)