from typing import List


def jacobi_iteration(A: List[List[float]],
                     b: List[float],
                     x: List[float]) -> List[float]:
    n = len(A)
    x_new = [0.0] * n
    for i in range(n):
        sum_val = sum(A[i][j] * x[j] for j in range(n) if j != i)
        x_new[i] = (b[i] - sum_val) / A[i][i]
    return x_new


def jacobi(A: List[List[float]],
           b: List[float],
           x0: List[float],
           tol: float,
           max_iter: int) -> [List[float], int]:
    n = len(A)
    x = x0.copy()
    iterate = 0

    while iterate < max_iter:
        x_new = jacobi_iteration(A, b, x)

        if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:
            return x_new, iterate

        x = x_new
        iterate += 1
        print(f'Вид матрицы на итерации {iterate}: ')
        print(x)

    return x, iterate


def seidel_iteration(A: List[List[float]],
                     b: List[float],
                     x: List[float]) -> List[float]:
    x_new = x.copy()
    n = len(A)
    for i in range(n):
        sum1 = sum(A[i][j] * x_new[j] for j in range(i))
        sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
    return x_new


def seidel(A: List[List[float]],
           b: List[float],
           x0: List[float],
           tol: float,
           max_iter: int) -> [List[float], int]:
    n = len(A)
    x = x0.copy()
    iterate = 0

    while iterate < max_iter:
        x_new = seidel_iteration(A, b, x)

        if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:
            return x_new, iterate

        x = x_new
        iterate += 1
        print(f'Вид матрицы на итерации {iterate}')
        print(x)

    return x, iterate


if __name__ == "__main__":
    A = [
        [4, -1, 0, 0],
        [-1, 4, -1, 0],
        [0, -1, 4, -1],
        [0, 0, -1, 3]
    ]
    b = [15, 10, 10, 10]
    x0 = [0, 0, 0, 0]


    print("Ответ полученный методом Якоби")
    sol_jac, iterate_jac = jacobi(A, b, x0, 1e-6, 1000)
    print()
    print()


    print("Ответ полученный методом Зейделя")
    sol_seidel, iterate_seidel = seidel(A, b, x0, 1e-6, 1000)

    print()
    print()

    print("Финальные результаты полученные методами")
    print(sol_jac)
    print(sol_seidel)

    print()
    print()

    print("За какое количество итераций сошелся каждый из методов")
    print("Якоби", iterate_jac)
    print("Зейдель", iterate_seidel)
