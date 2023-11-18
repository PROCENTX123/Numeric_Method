from Matrix import Matrix
from Vector import Vector
import numpy as np

def generate_matrix_and_vectors(matrix_vectors, size, left_border, right_border, diagonal_value):
    matrix = []
    vectors = []
    trues = []
    diagonal_demos = []

    diagonal_values = [i * (diagonal_value[1] - diagonal_value[0]) / (matrix_vectors - 1) + diagonal_value[0] for i in range(matrix_vectors)]

    for diagonal_demo in diagonal_values:
        matrix1 = Matrix.fill_random(size, left_border, right_border, diagonal_demo)
        vector1 = Vector.fill_random(size)

        mul_vector = matrix1 * vector1

        matrix.append(matrix1)
        vectors.append(mul_vector)
        trues.append(vector1)
        diagonal_demos.append(diagonal_demo)

    return matrix, vectors, trues, diagonal_demos

def get_input():

    matrix_vectors = int(input("Введите количество матриц и векторов: "))
    size = int(input("Введите размерность: "))
    left_border = int(input("Введите левую границу для значений в матрице: "))
    right_border = int(input("Введите правую границу для значений в матрице: "))
    left_border_diagonal = int(input("Введите левую границу для значения диагонали: "))
    right_border_diagonal = int(input("Введите правую границу для значения диагонали: "))

    return matrix_vectors, size, left_border, right_border, left_border_diagonal, right_border_diagonal

def Jakobi(A, b, x0, tol = 1e-10, max_iter = 1000):
    # n = vector.size()
    # A = np.array(matrix.grid, dtype=float)
    # b = np.array(vector.value, dtype=float)
    n = len(vector)

    x = np.copy(x0)

    for k in range(max_iter):
        x_old = np.copy(x)
        for i in range(n):
            sigma = np.dot(A[i, :i], x_old[:i]) + np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - sigma) / A[i, i]

            if np.linalg.norm(x - x_old, ord=np.inf) < tol:
                return x

    raise ValueError("Метод не сошелся за указанное количество итераций")



if __name__ == "__main__":
    # m1 = Matrix.input(3)

    # matrix = Matrix.fill_random(4, -5, 5, 1)
    # vector = Vector.fill_random(4)
    # x0 = np.zeros_like(vector)

    matrix = np.array([[4, -1, 0, 0],
              [-1, 4, -1, 0],
              [0, -1, 4, -1],
              [0, 0, -1, 4]], dtype=float)

    vector = np.array([15, 10, 10, 10], dtype=float)

    x0 = np.zeros_like(vector)

    solution = Jakobi(matrix, vector, x0)
    print(solution)
