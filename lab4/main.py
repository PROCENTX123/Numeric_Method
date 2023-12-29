from calc_methods import calc_eigen_values, calc_eigen_intervals, calc_eigen_vectors, calc_frobenius_eigen_vectors,\
    calc_gershgorin_round
from frobenius import frobenius_normal_form, union_intervals
from printer import prtinter
import numpy as np


def gen_sym_matrix(size: int,
                   a: int,
                   b: int) -> np.ndarray:
    matrix = np.random.uniform(a, b, (size, size))
    matrix_sym = (matrix + matrix.T) / 2
    return matrix_sym


def check_ort(size, eigen_orts, rtol=1e-5, atol=1e-8):
    return np.allclose(eigen_orts.dot(eigen_orts.T), np.identity(size), rtol, atol)


if __name__ == "__main__":
    size_matrix = int(input("Введите размер матрицы:", ))
    matrix = gen_sym_matrix(size_matrix, 0, 5)

    frobenius_matrix, frobenius_transform = frobenius_normal_form(size_matrix, matrix)

    char_poly = np.concatenate((np.array([(-1) ** size_matrix]), (-1) ** (size_matrix + 1) * frobenius_matrix[0]))

    intervals = calc_gershgorin_round(size_matrix, matrix)

    reduced_intervals = union_intervals(intervals)

    eigen_intervals = calc_eigen_intervals(reduced_intervals, divide_times=100)

    eigen_values = calc_eigen_values(eigen_intervals, delta=1e-2)

    frobenius_eigen_vectors = calc_frobenius_eigen_vectors(size_matrix, eigen_values)

    eigen_vectors = calc_eigen_vectors(frobenius_eigen_vectors, frobenius_transform, ort=True)

    prtinter()
