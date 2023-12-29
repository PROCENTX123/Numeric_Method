import random
from Vector import Vector

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
        matrix = [row + [vector.value[i]] for i, row in enumerate(self.grid)]

        for i in range(n):
            max_index = i
            for j in range(i+1, n):
                if abs(matrix[j][i]) > abs(matrix[max_index][i]):
                    max_index = j
            matrix[i], matrix[max_index] = matrix[max_index], matrix[i]

            for j in range(i+1, n):
                factor = matrix[j][i] / matrix[i][i]
                for k in range(i, n+1):
                    matrix[j][k] -= factor * matrix[i][k]

        x = [0] * n
        for i in range(n-1, -1, -1):
            x[i] = matrix[i][n] / matrix[i][i]
            for j in range(i-1, -1, -1):
                matrix[j][n] -= matrix[j][i] * x[i]
        return Vector(x)

