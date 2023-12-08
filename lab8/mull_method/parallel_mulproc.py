from multiprocessing import Pool
import numpy as np

def multiply_submatrices(args):

    sub_A, sub_B = args

    return np.dot(sub_A, sub_B)

def strassen_mul_mulproc(A, B, num_processes, size):
    submatrices = []

    n = len(A)
    mid = n // num_processes

    for i in range(num_processes):
        for j in range(num_processes):
            sub_A = A[i * mid: (i + 1) * mid, j * mid: (j + 1) * mid]
            sub_B = B[i * mid: (i + 1) * mid, j * mid: (j + 1) * mid]
            submatrices.append((sub_A, sub_B))

    with Pool(num_processes * num_processes) as pool:
        results = pool.map(multiply_submatrices, submatrices)

    result_blocks = [[results[i * num_processes + j] for j in range(num_processes)] for i in range(num_processes)]
    result = np.block(result_blocks)

    return result
