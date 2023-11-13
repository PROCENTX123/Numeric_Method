from Vector import Vector

class Matrix:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.column = len(grid[0])

    def shape(self):
        return self.rows, self.column

    def __mul__(self, other):

        if isinstance(other, Matrix):
            if self.rows != other.column:
                raise ValueError("Невозможно посчитать произведение")

            result = []
            for i in range(self.rows):
                row = []
                for j in range(other.column):
                    element = 0
                    for k in range(self.column):
                        element += self.grid[i][k] * other.grid[k][j]
                    row.append(element)
                result.append(row)
            return result

        elif isinstance(other, Vector):
            if self.column != other.size():
                raise ValueError("Невозможно посчитать произведение")

            result = []
            for i in range(self.rows):
                element = 0
                for j in range (self.column):
                    element += self.grid[i][j] * other.value[j]
                result.append(element)
            return result

        else:
            raise ValueError("Введены могут быть только матрицы или векторы")

    def transpose(self):
        transposed_matrix = [[self.grid[j][i] for j in range (self.rows)] for i in range (self.column)]
        return transposed_matrix
