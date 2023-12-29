from Matrix import Matrix
from Vector import Vector
from Graph import graph


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


if __name__ == "__main__":

    matrix_vectors, size, left_border, right_border, left_border_diagonal, right_border_diagonal = get_input()

    matrix, vectors, trues, diagonal_demos = generate_matrix_and_vectors(matrix_vectors, size, left_border, right_border, [left_border_diagonal, right_border_diagonal])
    graph(matrix, vectors, trues, diagonal_demos)


