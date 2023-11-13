from Vector import Vector
from Matrix import Matrix
from Graphic import draw
from Calc import calc_inaccuracy

if __name__ == "__main__":
    vector1 = Vector([1, 2, 3])
    vector2 = Vector([2, 3, 4])

    print(vector1 * vector2)
    print(vector1.normalize())

    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])

    print(matrix1 * matrix2)
    print(matrix1.transpose())


    m1 = Matrix([[1, 2], [3, 4]])
    v1 = Vector([5, 6])
    print(m1 * v1)


    # func = input()
    # us_func = lambda x: eval(func)
    # draw(us_func, -5, 5)

    calc_inaccuracy(7/5)
    calc_inaccuracy(17/12)