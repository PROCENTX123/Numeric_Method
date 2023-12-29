import numpy as np
import math
from typing import List, Union

def calc_gershgorin_round(size: int,
                          matrix: np.ndarray) -> List[List]:
    intervals = []
    for i in range(size):
        row_abs_sum = abs(matrix[i]).sum()
        center = matrix[i][i]
        radius = row_abs_sum - abs(center)
        intervals.append([center - radius, center + radius])
    return intervals


def calc_eigen_intervals(reduced_intervals,
                         divide_times=100) -> List[List[Union[float, int]]]:
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


