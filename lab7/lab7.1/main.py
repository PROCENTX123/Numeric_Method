from typing import List
import math

def cholesky(A: List[List[float]]) -> List[List[float]]:
    n = len(A)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            sum_val = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = math.sqrt(A[i][i] - sum_val)
            else:
                L[i][j] = (A[i][j] - sum_val) / L[j][j]
    return L


if __name__ == "__main__":
    A = [
        [4, -1, 0, 0],
        [-1, 4, -1, 0],
        [0, -1, 4, -1],
        [0, 0, -1, 3]
    ]

    L = cholesky(A)
    print("Разложение Холецкого")
    for row in L:
        print(row)

    #проверить это разложение можно на сайте https://mxncalc.com/ru/cholesky-decomposition
