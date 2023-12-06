from multiprocessing import Process, Queue

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

def strassen_mul_helper(A, B, queue):
    result = strassen_mul_mulproc(A, B)
    queue.put(result)

def strassen_mul_mulproc(A, B):
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]

    a11, a12, a21, a22 = split_matrix(A)
    b11, b12, b21, b22 = split_matrix(B)

    queue = Queue()

    processes = []

    processes.append(Process(target=strassen_mul_helper, args=(add(a11, a22), add(b11, b22), queue)))
    processes.append(Process(target=strassen_mul_helper, args=(add(a21, a22), b11, queue)))
    processes.append(Process(target=strassen_mul_helper, args=(a11, sub(b12, b22), queue)))
    processes.append(Process(target=strassen_mul_helper, args=(a22, sub(b21, b11), queue)))
    processes.append(Process(target=strassen_mul_helper, args=(add(a11, a12), b22, queue)))
    processes.append(Process(target=strassen_mul_helper, args=(sub(a21, a11), add(b11, b12), queue)))
    processes.append(Process(target=strassen_mul_helper, args=(sub(a12, a22), add(b21, b22), queue)))

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    p1, p2, p3, p4, p5, p6, p7 = [queue.get() for _ in range(7)]

    c11 = add(sub(add(p1, p4), p5), p7)
    c12 = add(p3, p5)
    c21 = add(p2, p4)
    c22 = add(sub(add(p1, p3), p2), p6)

    result = c11 + c12 + c21 + c22
    return result

