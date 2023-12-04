import threading
from .strassen import strassen_mul


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

    results = {}

    threads = [
        threading.Thread(target=lambda: results.update({'p1': strassen_mul(add(a11, a22), add(b11, b22))})),
        threading.Thread(target=lambda: results.update({'p2': strassen_mul(add(a21, a22), b11)})),
        threading.Thread(target=lambda: results.update({'p3': strassen_mul(a11, sub(b12, b22))})),
        threading.Thread(target=lambda: results.update({'p4': strassen_mul(a22, sub(b21, b11))})),
        threading.Thread(target=lambda: results.update({'p5': strassen_mul(add(a11, a12), b22)})),
        threading.Thread(target=lambda: results.update({'p6': strassen_mul(sub(a21, a11), add(b11, b12))})),
        threading.Thread(target=lambda: results.update({'p7': strassen_mul(sub(a12, a22), add(b21, b22))}))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    p1 = results['p1']
    p2 = results['p2']
    p3 = results['p3']
    p4 = results['p4']
    p5 = results['p5']
    p6 = results['p6']
    p7 = results['p7']

    c11 = add(sub(add(p1, p4), p5), p7)
    c12 = add(p3, p5)
    c21 = add(p2, p4)
    c22 = add(sub(add(p1, p3), p2), p6)

    result = c11 + c12 + c21 + c22
    return result