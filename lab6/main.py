import numpy as np
from generators import generate_random_vector, generate_symmetric_matrix
from graphic import show_func


def find_eigens_with_krylov_method(matrix):
    n = len(matrix)
    y = np.eye(n)[0]
    B = []
    B.append(y)

    for _ in range(1, n):
        y = matrix @ y
        B.append(y)

    y = matrix @ y
    p = np.linalg.solve(np.array(B).T, y)
    coeffs = [1] + list(- p[::-1])
    eigenvalues = np.roots(coeffs)

    y = np.array(B)

    q = np.zeros((n, n))
    eigenvectors = []
    for i in range(n):
        xi = np.zeros(n)
        for j in range(n):
            if j == 0:
                q[j][i] = 1
            else:
                q[j][i] = eigenvalues[i] * q[j - 1][i] - p[n - j]

            xi += q[j][i] * y[n - 1 - j]
        eigenvectors.append(xi)

    return eigenvalues, eigenvectors


def one_parameter(A, b, x0, t, eps=1e-6):
    n = len(A)
    x = x0.copy()
    k = 0

    P = np.eye(n) - t * A
    g = t * b

    while True:
        x_new = P @ x+g
        k += 1

        if np.linalg.norm(x_new - x) < eps:
            break

        x = x_new

    return x, k


if __name__ == "__main__":
    n = int(input('Введите размер матрицы:', ))
    A = generate_symmetric_matrix(n, 0, 1, diag=20)
    x_true = generate_random_vector(n, 1, 5)
    b = A @ x_true
    eigenvalues, eigenvectors = find_eigens_with_krylov_method(A)

    eigen_min = min(eigenvalues)
    eigen_max = max(eigenvalues)

    t_opt = 2 / (eigen_min + eigen_max)

    print(t_opt)

    x, k = one_parameter(A, b, generate_random_vector(n, -1, 1),  t_opt)

    t_range = np.arange(0.001, 2 / eigen_max, 0.003)
    x0 = generate_random_vector(n, -1, 1)
    iterations = [one_parameter(A, b, x0, t)[1] for t in t_range]

    show_func(iterations, t_range)
