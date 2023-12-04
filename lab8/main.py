import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def split_matrix(matrix):
    size = len(matrix)
    mid = size // 2
    a11 = [row[:mid] for row in matrix[:mid]]
    a12 = [row[mid:] for row in matrix[:mid]]
    a21 = [row[:mid] for row in matrix[mid:]]
    a22 = [row[mid:] for row in matrix[mid:]]
    return a11, a12, a21, a22


def strassen_mul_parallel(A, B):
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]

    a11, a12, a21, a22 = split_matrix(A)
    b11, b12, b21, b22 = split_matrix(B)

    with ThreadPoolExecutor(max_workers=7) as executor:
        futures = [
            executor.submit(strassen_mul_parallel, add(a11, a22), add(b11, b22)),
            executor.submit(strassen_mul_parallel, add(a21, a22), b11),
            executor.submit(strassen_mul_parallel, a11, sub(b12, b22)),
            executor.submit(strassen_mul_parallel, a22, sub(b21, b11)),
            executor.submit(strassen_mul_parallel, add(a11, a12), b22),
            executor.submit(strassen_mul_parallel, sub(a21, a11), add(b11, b12)),
            executor.submit(strassen_mul_parallel, sub(a12, a22), add(b21, b22)),
        ]

    p1_result, p2_result, p3_result, p4_result, p5_result, p6_result, p7_result = [future.result() for future in futures]

    c11 = add(sub(add(p1_result, p4_result), p5_result), p7_result)
    c12 = add(p3_result, p5_result)
    c21 = add(p2_result, p4_result)
    c22 = add(sub(add(p1_result, p3_result), p2_result), p6_result)

    result = c11 + c12 + c21 + c22
    return result

def strassen_mul(A, B):
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]

    a11, a12, a21, a22 = split_matrix(A)
    b11, b12, b21, b22 = split_matrix(B)

    p1 = strassen_mul(add(a11, a22), add(b11, b22))
    p2 = strassen_mul(add(a21, a22), b11)
    p3 = strassen_mul(a11, sub(b12, b22))
    p4 = strassen_mul(a22, sub(b21, b11))
    p5 = strassen_mul(add(a11, a12), b22)
    p6 = strassen_mul(sub(a21, a11), add(b11, b12))
    p7 = strassen_mul(sub(a12, a22), add(b21, b22))

    c11 = add(sub(add(p1, p4), p5), p7)
    c12 = add(p3, p5)
    c21 = add(p2, p4)
    c22 = add(sub(add(p1, p3), p2), p6)

    result = c11 + c12 + c21 + c22
    return result


def filling_matrix(rows, columns, matrix):
    for i in range(rows):
        row = []
        for j in range(columns):
            element = float(input())
            row.append(element)
        matrix.append(row)


def matrix_multuply(A, B):
    C = [[0.0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C


if __name__ == "__main__":
    dimension = 64

    matrix_A = np.random.randint(low=0, high=10, size=(dimension, dimension))
    matrix_B = np.random.randint(low=0, high=10, size=(dimension, dimension))

    start_time_strassen = time.time()
    strassen_mul_result = strassen_mul(matrix_A, matrix_B)
    end_time_strassen = time.time()
    execution_time_strassen = end_time_strassen - start_time_strassen

    start_time_common = time.time()
    common_mul_result = matrix_multuply(matrix_A, matrix_B)
    end_time_common = time.time()
    execution_time_common = end_time_common - start_time_common


    start_time_parallel = time.time()
    strassen_mul_parallel_result = strassen_mul_parallel(matrix_A, matrix_B)
    end_time_parallel = time.time()
    execution_time_parallel = end_time_parallel - start_time_parallel

    # print(strassen_mul_result)
    # print(strassen_mul_parallel_result)
    # print(common_mul_result)

    print(execution_time_strassen)
    print(execution_time_common)
    print(execution_time_parallel)
