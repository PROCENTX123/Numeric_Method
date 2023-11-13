from Matrix import Matrix
from Vector import Vector
import numpy as np
import copy

if __name__ == "__main__":
    # m1 = Matrix.input(3)

    v1 = Vector([10, 15, -5])
    m2 = Matrix.fill_random(3, -10, 10, 4)

    b = m2 * v1

    x_chisl = m2.gauss(b)

    x_bibil = Vector(list(np.linalg.solve(copy.deepcopy(m2.grid), copy.deepcopy(b.value))))

    print((v1.sub(x_chisl)).normalize())
    print((v1.sub(x_bibil)).normalize())