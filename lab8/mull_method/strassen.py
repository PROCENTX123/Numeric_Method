from .common_method import matrix_multuply

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


def strassen_mul(A, B):
    # if len(A) == 1:
    #     return [[A[0][0] * B[0][0]]]

    if len(A) <= 64:
        return matrix_multuply(A, B)

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

def strassen_mul_check(A, B, to_common):
    if len(A) <= to_common:
        return matrix_multuply(A, B)

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

