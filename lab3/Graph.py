from Matrix import Matrix
from Vector import Vector
import matplotlib.pyplot as plt
import copy

def graph(matrix: [Matrix], vectors:[Vector], trues, diagonal_demos):
    x_gauss_columns_norms = []
    x_gauss_rows_norms = []
    x_gauss_columns_rows_norms = []
    x_gauss_orig_norms = []
    diag_dem_values = []

    for A, b, x, diag_demo in zip(matrix, vectors, trues, diagonal_demos):
        x_gauss = A.gauss(copy.deepcopy(b))
        x_gauss_rows = A.gauss_permutation_row(copy.deepcopy(b))
        x_gauss_columns = A.gauss_permutation_colon(copy.deepcopy(b))
        x_gauss_columns_rows = A.gauss_permutation_row_and_colon(copy.deepcopy(b))


        x_gauss_columns_norm = x.sub(x_gauss_columns).normalize()
        x_gauss_rows_norm = x.sub(x_gauss_rows).normalize()
        x_gauss_columns_rows_norm = x.sub(x_gauss_columns_rows).normalize()
        x_orig = x.sub(x_gauss).normalize()

        x_gauss_columns_norms.append(x_gauss_columns_norm)
        x_gauss_rows_norms.append(x_gauss_rows_norm)
        x_gauss_columns_rows_norms.append(x_gauss_columns_rows_norm)
        x_gauss_orig_norms.append(x_orig)
        diag_dem_values.append(diag_demo)

    plt.plot(diag_dem_values, x_gauss_orig_norms, label='Orig')
    plt.plot(diag_dem_values, x_gauss_rows_norms, label='Rows')
    plt.plot(diag_dem_values, x_gauss_columns_norms, label='Columns')
    plt.plot(diag_dem_values, x_gauss_columns_rows_norms, label='Columns and Rows')



    plt.xlabel('Диагональный доминант')
    plt.ylabel('Error')

    plt.legend()
    plt.savefig("Graph1.png")
