import numpy as np
from typing import Tuple, List


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
