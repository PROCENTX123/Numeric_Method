import copy
import random
from Vector import Vector
import numpy as np

class Matrix:
    def __init__(self, grid):
        self.grid = grid
        self.row = len(grid)
        self.column = len(grid[0])

    def shape(self):
        return self.row, self.column

    @classmethod
    def input(cls, n):
        values = []
        for _ in range(n):
            row = []
            for _ in range(n):
                element = float(input("Введите значения для матрицы "))
                row.append(element)
            values.append(row)
        return cls(values)

    @classmethod
    def fill_random(cls, n: int, left_border: int, right_border: int, diagonal_value: int):
        values = []
        for i in range(n):
            row = []
            for j in range(n):
                if i == j:
                    element = random.uniform(left_border + diagonal_value, right_border)
                else:
                    element = random.uniform(left_border, right_border)
                row.append(element)
            values.append(row)
        return cls(values)

    def __mul__(self, other):

        if isinstance(other, Matrix):
            if self.row != other.column:
                raise ValueError("Невозможно посчитать произведение")

            result = []
            for i in range(self.row):
                row = []
                for j in range(other.column):
                    element = 0
                    for k in range(self.column):
                        element += self.grid[i][k] * other.grid[k][j]
                    row.append(element)
                result.append(row)
            return Matrix(result)

        elif isinstance(other, Vector):
            if self.column != other.size():
                raise ValueError("Невозможно посчитать произведение")

            result = []
            for i in range(self.row):
                element = 0
                for j in range(self.column):
                    element += self.grid[i][j] * other.value[j]
                result.append(element)
            return Vector(result)

        else:
            raise ValueError("Введены могут быть только матрицы или векторы")

    def gauss(self, vector):
        n = vector.size()
        vector = np.array(copy.deepcopy(vector.value), dtype=float)
        matrix = np.array(copy.deepcopy(self.grid), dtype=float)
        x = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                factor = matrix[j][i] / matrix[i][i]
                for k in range(i, n):
                    if k != i:
                        matrix[j][k] -= factor * matrix[i][k]
                vector[j] -= factor * vector[i]

        for i in range(n - 1, -1, -1):
            x[i] = vector[i]
            for j in range(n - 1, i, -1):
                x[i] -= x[j] * matrix[i][j]
            x[i] /= matrix[i][i]

        return Vector(x)

    def gauss_permutation_row(self, vector):
        n = vector.size()
        matrix = np.array(copy.deepcopy(self.grid), dtype=float)
        vector = np.array(copy.deepcopy(vector.value), dtype=float)
        x = np.zeros(n, dtype=float)

        for i in range(n):
            max_index = i
            for j in range(i + 1, n):
                if abs(matrix[j][i]) > abs(matrix[max_index][i]):
                    max_index = j

            if max_index != i:
                matrix[[i, max_index]] = matrix[[max_index, i]]
                vector[i], vector[max_index] = vector[max_index], vector[i]

            for j in range(i + 1, n):
                factor = matrix[j][i] / matrix[i][i]
                for k in range(i, n):
                    if k != i:
                        matrix[j][k] -= factor * matrix[i][k]
                vector[j] -= factor * vector[i]

        for i in range(n - 1, -1, -1):
            x[i] = vector[i]
            for j in range(n - 1, -1, -1):
                if j != i:
                    x[i] -= x[j] * matrix[i][j]
            x[i] /= matrix[i][i]

        return Vector(x)

    def gauss_permutation_colon(self, vector):
        n = vector.size()
        matrix = np.array(copy.deepcopy(self.grid), dtype=float)
        vector = np.array(copy.deepcopy(vector.value), dtype=float)
        x = np.zeros(n, dtype=float)
        perm = [i for i in range(n)]

        for i in range(n):
            max_index = i
            for j in range(i + 1, n):
                if abs(matrix[i][j]) > abs(matrix[i][max_index]):
                    max_index = j

            if max_index != i:
                for k in range(n):
                    matrix[k][i], matrix[k][max_index] = matrix[k][max_index], matrix[k][i]
                perm[i], perm[max_index] = perm[max_index], perm[i]

            for j in range(i + 1, n):
                factor = matrix[j][i] / matrix[i][i]
                for k in range(i, n):
                    if k != i:
                        matrix[j][k] -= factor * matrix[i][k]
                vector[j] -= factor * vector[i]

        x1 = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x1[i] = vector[i]
            for j in range(n - 1, i, -1):
                if j != i:
                    x1[i] -= x1[j] * matrix[i][j]
            x1[i] /= matrix[i][i]

        for i in range(n):
            x[perm[i]] = x1[i]

        return Vector(x)

    # def gauss_permutation_row_and_colon(self, vector):
    #     n = vector.size()
    #     matrix = np.array(copy.deepcopy(self.grid), dtype=float)
    #     vector = np.array(copy.deepcopy(vector.value), dtype=float)
    #     x = np.zeros(n, dtype=float)
    #     perm = [i for i in range(n)]
    #
    #     for i in range(n):
    #         max_index_str = i
    #         for j in range(i + 1, n):
    #             if abs(matrix[j][i]) > abs(matrix[max_index_str][i]):
    #                 max_index_str = j
    #
    #         max_index_col = i
    #         for j in range(i + 1, n):
    #             if abs(matrix[i][j]) > abs(matrix[i][max_index_col]):
    #                 max_index_col = j
    #
    #         if max_index_str != i or max_index_col != i:
    #
    #             if max_index_str > max_index_col:
    #                 for k in range(n):
    #                     matrix[i][k], matrix[max_index_str][k] = matrix[max_index_str][k], matrix[i][k]
    #                 vector[i], vector[max_index_str] = vector[max_index_str], vector[i]
    #
    #             else:
    #                 for k in range(n):
    #                     matrix[k][i], matrix[k][max_index_col] = matrix[max_index_col][k], matrix[k][i]
    #                 perm[i], perm[max_index_col] = perm[max_index_col], perm[i]
    #
    #         for j in range(i + 1, n):
    #             factor = matrix[j][i] / matrix[i][i]
    #             for k in range(i, n):
    #                 if k != i:
    #                     matrix[j][k] -= factor * matrix[i][k]
    #             vector[j] -= factor * vector[i]
    #
    #     x1 = np.zeros(n)
    #     for i in range(n - 1, -1, -1):
    #         x1[i] = vector[i]
    #         for j in range(n - 1, i, -1):
    #             x1[i] -= x1[j] * matrix[i][j]
    #         x1[i] /= matrix[i][i]
    #
    #     for i in range(n):
    #         x[perm[i]] = x1[i]
    #
    #     return Vector(x)

    def gauss_permutation_row_and_colon(self, vector):
        n = vector.size()
        matrix = np.array(copy.deepcopy(self.grid), dtype=float)
        vector = np.array(copy.deepcopy(vector.value), dtype=float)
        x = np.zeros(n, dtype=float)
        perm = [i for i in range(n)]

        for i in range(n - 1):
            max_row = np.argmax(np.abs(matrix[i:, i])) + i
            max_col = np.argmax(np.abs(matrix[i, i:])) + i
            if matrix[max_col][i] > matrix[i][max_row]:
                matrix[[i, max_col]] = matrix[[max_col, i]]
                vector[i], vector[max_col] = vector[max_col], vector[i]
            else:
                perm[i], perm[max_row] = perm[max_row], perm[i]
                for j in range(n):
                    matrix[j][i], matrix[j][max_row] = matrix[j][max_row], matrix[j][i]

            for j in range(i + 1, n):
                f = matrix[j][i] / matrix[i][i]
                matrix[j] -= f * matrix[i]
                vector[j] -= f * vector[i]

        for i in range(n - 1, -1, -1):
            x[i] = vector[i] / matrix[i][i]
            for j in range(i - 1, -1, -1):
                vector[j] -= matrix[j][i] * x[i]

        x_copy = copy.deepcopy(x)

        for i, order in enumerate(perm):
            x[order] = x_copy[i]

        return Vector(x)
