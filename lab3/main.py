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

if __name__ == "__main__":
    # m1 = Matrix.input(3)

    matrix, vectors, trues, diagonal_demos = generate_matrix_and_vectors(300, 300, -10, 10, [-600, 1000])
    graph(matrix, vectors, trues, diagonal_demos)


