import numpy as np


def generate_random_vector(dim: int, a: float, b: float):
    return np.random.uniform(a, b, dim)

def generate_symmetric_matrix(dim: int, a: float, b: float, diag: int = 10):
    matrix = np.random.uniform(a, b, size=(dim, dim))
    symmetric_matrix = np.triu(matrix) + np.triu(matrix, 1).T

    symmetric_matrix += np.eye(dim)*diag
    return symmetric_matrix
