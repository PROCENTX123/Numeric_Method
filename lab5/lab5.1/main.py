from typing import List

def jacobi_iteration(A: List[List[float]], b: List[float], x: List[float]) -> List[float]:
    n = len(A)
    x_new = [0.0] * n
    for i in range(n):
        sum_val = sum(A[i][j] * x[j] for j in range(n) if j != i)
        x_new[i] = (b[i] - sum_val) / A[i][i]
    return x_new

def jacobi(A: List[List[float]], b: List[float], x0: List[float], tol: float, max_iter: int) -> List[float]:
    n = len(A)
    x = x0.copy()
    iterate = 0

    while iterate < max_iter:
        x_new = jacobi_iteration(A, b, x)

        if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:
            return x_new

        x = x_new
        iterate += 1
        print(f'Вид матрицы на итерации {iterate}: ')
        print(x)

    return x

def gaussian_elimination(A: List[List[float]], b: List[float]) -> List[float]:
    n = len(A)
    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i):
            b[j] -= A[j][i] * x[i]

    return x

if __name__ == "__main__":
    # Пробные входные данные
    A = [
        [4, -1, 0, 0],
        [-1, 4, -1, 0],
        [0, -1, 4, -1],
        [0, 0, -1, 3]
    ]
    b = [15, 10, 10, 10]
    x0 = [0, 0, 0, 0]

    # Решение методом Якоби
    sol_jac = jacobi(A, b, x0, 1e-6, 200)

    # Решение методом Гаусса
    sol_gauss = gaussian_elimination(A, b)

    print('Ответ используя метод Якоби: ')
    print(sol_jac)
    print('Ответ используя метод Гаусса: ')
    print(sol_gauss)

    # Проверка того, что результаты методов отличаются меньше чем на эпсилон
    print("Сравнение методов:", all(abs(sol_jac[i] - sol_gauss[i]) < 1e-6 for i in range(len(sol_jac))))

    # Проверка на диагональное преобладание
    diagonal_dom = all(
        abs(A[i][i]) > sum(
            abs(A[i][j]) for j in range(len(A[i])) if j != i
        ) for i in range(len(A))
    )
    print("Диагональное преобладание:", diagonal_dom)

    P = [
        [-A[i][j] / A[i][i] if i != j else 0 for j in range(len(A[i]))]
        for i in range(len(A))
    ]

    norm_P = max(
        sum(
            abs(P[i][j]) for j in range(len(P[i]))
        ) for i in range(len(P))
    )

    q = 0.9

    if norm_P <= q:
        print("Выполнение условия:", True)
    else:
        print("Выполнение условия:", False)
