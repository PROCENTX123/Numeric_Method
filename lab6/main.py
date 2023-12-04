import numpy as np

def gen_vector(n: int, a: float, b: float):
    vector = np.random.uniform(a, b, size=n)
    return vector

def gem_matrix(n: int, a: float, b: float, diag: int = 10):
    matrix = np.random.uniform(a, b, size=(n, n))
    sym_matrix = np.triu(matrix) + np.triu(matrix, 1).T

    sym_matrix += np.eye(n) * diag
    return sym_matrix

if __name__ == "__main__":
    vector = gen_vector(5, 1, 5)