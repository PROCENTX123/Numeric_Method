import numpy as np
import time
from mull_method.common_method import matrix_multuply
from mull_method.strassen import strassen_mul
from mull_method.parallel import strassen_mul_parallel
from mull_method.parallel_mulproc import strassen_mul_mulproc
import matplotlib.pyplot as plt

def graphic(time_common, time_strassen, time_parallel, time_mulproc):
    plt.figure(figsize=(8, 6))

    plt.plot(sizes, time_common, label='Common Multiplication', marker='o')
    plt.plot(sizes, time_strassen, label='Strassen Multiplication', marker='o')
    plt.plot(sizes, time_parallel, label='Parallel Strassen Multiplication', marker='o')
    plt.plot(sizes, time_mulproc, label='Parallel Strassen Multiprocessing', marker='o')

    plt.grid(True, linestyle='--', alpha=0.7)

    plt.xlabel('Matrix Size')
    plt.ylabel('Execution Time ')
    plt.title('Matrix Multiplication Performance')
    plt.legend()

    plt.show()


if __name__ == "__main__":
    sizes = [2, 4, 8, 16, 32, 64, 128]

    time_common = []
    time_strassen = []
    time_parallel = []
    time_mulproc = []

    for size in sizes:

        matrix_A = np.random.randint(low=0, high=10, size=(size, size))
        matrix_B = np.random.randint(low=0, high=10, size=(size, size))

        start_time_strassen = time.time()
        strassen_mul_result = strassen_mul(matrix_A, matrix_B)
        end_time_strassen = time.time()
        execution_time_strassen = end_time_strassen - start_time_strassen
        time_strassen.append(execution_time_strassen)

        start_time_common = time.time()
        common_mul_result = matrix_multuply(matrix_A, matrix_B)
        end_time_common = time.time()
        execution_time_common = end_time_common - start_time_common
        time_common.append(execution_time_common)

        start_time_mulproc = time.time()
        strassen_mulproc_res = strassen_mul_mulproc(matrix_A, matrix_B)
        end_time_mulproc = time.time()
        execution_time_mulptoc = end_time_mulproc - start_time_mulproc
        time_mulproc.append(execution_time_mulptoc)

        start_time_parallel = time.time()
        strassen_mul_parallel_result = strassen_mul_parallel(matrix_A, matrix_B)
        end_time_parallel = time.time()
        execution_time_parallel = end_time_parallel - start_time_parallel
        time_parallel.append(execution_time_parallel)

    graphic(time_common, time_strassen, time_parallel, time_mulproc)
