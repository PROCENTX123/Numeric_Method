import numpy as np

def SVD(matrix):


    matrixTmatrix = np.dot(matrix.T, matrix)

    #Собственные значения
    eigenvalues, eigenvectors = np.linalg.eig(matrixTmatrix)

    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]


    singular_values = np.sqrt(eigenvalues)

    Sigma = np.diag(singular_values)
    # nonzero_cols = np.any(Sigma != 0, axis=0)
    # nonzero_rows = np.any(Sigma != 0, axis=1)
    # Sigma = Sigma[nonzero_rows][:, nonzero_cols]

    #Унитарная матрица U
    U = matrix.dot(eigenvectors) / singular_values
    U = np.nan_to_num(U, nan=0.0, posinf=0.0, neginf=0.0)
    # nonzero_rows = np.any(U != 0, axis=1)
    # nonzero_cols = np.any(U != 0, axis=0)
    # U = U[nonzero_rows][:, nonzero_cols]

    #Транспонированная унитарная V
    V = eigenvectors.T

    return U, Sigma, V


if __name__ == "__main__":
    A = np.array([[3, 1, 1],
                  [-1, 3, 1]])

    U, S, VT = np.linalg.svd(A)
    U1, S1, VT1 = SVD(A)

    print("Matrix U:")
    print(U)
    print()
    print("matrix U1:")
    print(U1)
    print()
    print()
    print("matrix S:")
    print(S)
    print()
    print("matrix S1:")
    print(S1)
    print()
    print()
    print("matrix VT")
    print(VT)
    print("matrix VT1")
    print(VT1)

    print()
    print()

    print("check original matrix")
    check = U1 @ S1 @ VT1
    print("the matrix obtained by the product of U S VT")
    print(check)
    print("original matrix")
    print(A)
