import math

import numpy as np
from typing import Tuple, List, Union


def gen_sym_matrix(size: int,
                   a: int,
                   b: int) -> np.ndarray:
    matrix = np.random.uniform(a, b, (size, size))
    matrix_sym = (matrix + matrix.T) / 2
    return matrix_sym


def frobenius_normal_form(size: int,
                          matrix: np.ndarray) -> Tuple[np.ndarray,
                                                       np.ndarray]:
    temp_matrix = matrix
    reduction_matrix_prod = np.identity(size)

    for i in range(1, size):

        reduction_matrix = np.identity(size)
        reduction_matrix[size - i - 1, :] = -temp_matrix[size - i, :] / temp_matrix[size - i, size - i - 1]
        reduction_matrix[size - i - 1, size - i - 1] = 1 / temp_matrix[size - i, size - i - 1]

        reduction_matrix_prod = reduction_matrix_prod.dot(reduction_matrix)

        reduction_matrix_inv = np.identity(size)
        reduction_matrix_inv[size - i - 1, :] = temp_matrix[size - i, :]

        temp_matrix = reduction_matrix_inv @ temp_matrix @ reduction_matrix

    frobenius_matrix = temp_matrix

    return frobenius_matrix, reduction_matrix_prod


def calc_gershgorin_round(size: int,
                          matrix: np.ndarray) -> List[List]:
    intervals = []
    for i in range(size):
        row_abs_sum = abs(matrix[i]).sum()
        center = matrix[i][i]
        radius = row_abs_sum - abs(center)
        intervals.append([center - radius, center + radius])
    return intervals


def union_intervals(intervals: List[List]) -> List[List]:
    intervals.sort()
    reduced_intervals = []
    first_interval = intervals[0]

    for i in range(1, len(intervals)):

        current_interval = intervals[i]

        if current_interval[0] < first_interval[1]:
            first_interval[1] = max(first_interval[1], current_interval[1])
        else:
            reduced_intervals.append(first_interval)
            first_interval = current_interval

    reduced_intervals.append(first_interval)

    return reduced_intervals


def calc_eigen_intervals(reduced_intervals, divide_times=100) -> List[List[Union[float, int]]]:
    for interval in reduced_intervals:
        left, right = interval

        eigen_intervals = []

        value = np.polyval(char_poly, left)
        prev_x = left
        prev_sign = (value > 0)
        for x in np.linspace(left, right, divide_times):
            value = np.polyval(char_poly, x)
            cur_sign = (value > 0.)
            if prev_sign != cur_sign:
                eigen_intervals.append([prev_x, x])
                prev_x = x
                prev_sign = cur_sign

    return eigen_intervals


def calc_eigen_values(eigen_intervals, delta=1e-2) -> List:

    eigen_values = []

    for eigen_interval in eigen_intervals:
        left, right = eigen_interval

        left_value = (np.polyval(char_poly, left) > 0)

        approx_value = math.inf
        while abs(approx_value) > delta:
            approx_x = (left + right) / 2
            approx_value = np.polyval(char_poly, approx_x)

            if (approx_value > 0) == (left_value > 0):
                left = approx_x
            else:
                right = approx_x

        eigen_values.append(approx_x)

    eigen_values = np.array(eigen_values)

    return eigen_values


def calc_frobenius_eigen_vectors(size, eigen_values):
    frobenius_eigen_vectors = []

    for i in range(size - 1, -1, -1):
        frobenius_eigen_vectors.append(eigen_values ** i)

    frobenius_eigen_vectors = np.array(frobenius_eigen_vectors).T

    return frobenius_eigen_vectors


def calc_eigen_vectors(frobenius_eigen_vectors, frobenius_transform, ort=True):
    eigen_vectors = frobenius_eigen_vectors.dot(frobenius_transform.T)
    if ort:
        eigen_vectors = eigen_vectors / np.linalg.norm(eigen_vectors, axis=1)[:, None]

    return eigen_vectors


def check_ort(size, eigen_orts, rtol=1e-5, atol=1e-8):
    return np.allclose(eigen_orts.dot(eigen_orts.T), np.identity(size), rtol, atol)


if __name__ == "__main__":
    size_matrix = int(input())
    matrix = gen_sym_matrix(size_matrix, 0, 5)

    frobenius_matrix, frobenius_transform = frobenius_normal_form(size_matrix, matrix)

    char_poly = np.concatenate((np.array([(-1) ** size_matrix]), (-1) ** (size_matrix + 1) * frobenius_matrix[0]))

    intervals = calc_gershgorin_round(size_matrix, matrix)

    reduced_intervals = union_intervals(intervals)

    eigen_intervals = calc_eigen_intervals(reduced_intervals, divide_times=100)

    eigen_values = calc_eigen_values(eigen_intervals, delta=1e-2)

    frobenius_eigen_vectors = calc_frobenius_eigen_vectors(size_matrix, eigen_values)

    eigen_vectors = calc_eigen_vectors(frobenius_eigen_vectors, frobenius_transform, ort=True)

    print(check_ort(size_matrix, eigen_vectors, rtol=1e-2, atol=1e-2))