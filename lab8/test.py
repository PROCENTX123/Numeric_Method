import numpy as np
import matplotlib.pyplot as plt
from time import time
from multiprocessing import Pool


def mult_matrix(M, N):
    R = np.zeros((len(M), len(N[0])))
    for i in range(len(M)):
        for j in range(len(N[0])):
            for k in range(len(M[0])):
                R[i][j] += M[i][k] * N[k][j]
    return R


def split(matrix):
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]


def strassen(matrix1, matrix2):
    if len(matrix1) <= 64:
        return mult_matrix(matrix1, matrix2)

    a, b, c, d = split(matrix1)
    e, f, g, h = split(matrix2)

    p1 = strassen(a, f - h)
    p2 = strassen(a + b, h)
    p3 = strassen(c + d, e)
    p4 = strassen(d, g - e)
    p5 = strassen(a + d, e + h)
    p6 = strassen(b - d, g + h)
    p7 = strassen(a - c, e + f)

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p5 + p1 - p3 - p7

    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return c


def strassen_multi(matrix1, matrix2):
    if len(matrix1) <= 64:
        return mult_matrix(matrix1, matrix2)

    a, b, c, d = split(matrix1)
    e, f, g, h = split(matrix2)

    pool = Pool(processes=7)

    p1 = pool.apply_async(strassen, (a, f - h))
    p2 = pool.apply_async(strassen, (a + b, h))
    p3 = pool.apply_async(strassen, (c + d, e))
    p4 = pool.apply_async(strassen, (d, g - e))
    p5 = pool.apply_async(strassen, (a + d, e + h))
    p6 = pool.apply_async(strassen, (b - d, g + h))
    p7 = pool.apply_async(strassen, (a - c, e + f))

    p1 = p1.get()
    p2 = p2.get()
    p3 = p3.get()
    p4 = p4.get()
    p5 = p5.get()
    p6 = p6.get()
    p7 = p7.get()

    pool.close()
    pool.join()

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p5 + p1 - p3 - p7

    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return c


def main():
    time_strassen_list = []
    time_strassen_concurrent_list = []
    time_common_list = []
    size_list = [16, 32, 64, 128, 256]

    for size in size_list:
        mat1 = np.random.rand(size, size)
        mat2 = np.random.rand(size, size)

        time_begin = time()
        result_strassen = strassen(mat1, mat2)
        time_strassen = time()
        time_strassen_list.append(time_strassen - time_begin)

        start_time = time()
        result_common = mult_matrix(mat1, mat2)
        time_common = time()
        time_common_list.append(time_common - start_time)

        # _ = strassen_multi(mat1, mat2)
        # time_conc_strassen = time()
        # time_strassen_concurrent_list.append(time_conc_strassen - time_common)

    a = 1
    print("OOOkey")

    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(20)
    plt.plot(size_list, time_strassen_list, label="Strassen")
    plt.plot(size_list, time_common_list, label="Common")
    # plt.plot(size_list, time_strassen_concurrent_list, label="Strassen_conc")
    plt.xlabel("size")
    plt.ylabel("time")
    plt.legend()
    plt.show()

    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(20)
    plt.plot(size_list, time_strassen_list, label="Strassen")
    plt.plot(size_list, time_common_list, label="Common")
    plt.plot(size_list, time_strassen_concurrent_list, label="Strassen_conc")
    plt.xlabel("size")
    plt.ylabel("time")
    plt.ylim(0, 0.5)
    plt.xlim(50, 70)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
