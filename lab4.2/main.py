import numpy as np


def generate_random_vector(dim: int, a: float, b: float):
    return np.random.uniform(a, b, dim)


def generate_symmetric_matrix(dim: int, a: float, b: float, diag: int = 10):
    matrix = np.random.uniform(a, b, size=(dim, dim))
    symmetric_matrix = np.triu(matrix) + np.triu(matrix, 1).T

    symmetric_matrix += np.eye(dim)*diag
    return symmetric_matrix


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


if __name__ == "__main__":
    size = int(input('Ведите размер матрицы:', ))

    matrix = generate_symmetric_matrix(size, 0, 5)
    vector_true = generate_random_vector(size, 0, 5)

    b = matrix @ vector_true
    eigenvalues, eigenvectors = find_eigens_with_krylov_method(matrix)

    print('Собственные значения:')
    print(eigenvalues)

    print()
    print()

    print('Собственные вектора:')
    print(eigenvectors)
