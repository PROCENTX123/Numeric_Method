
def prtinter():
    from main import matrix, frobenius_matrix, frobenius_transform, char_poly, eigen_intervals, eigen_values, \
    frobenius_eigen_vectors, eigen_vectors, check_ort, size_matrix
    print('Исходная матрица:')
    print(matrix)

    print()
    print()

    print('Матрица Фробениуса:')
    print(frobenius_matrix)

    print()
    print()

    print('Матрица преобразования:')
    print(frobenius_transform)

    print()
    print()

    print('Характеристический многочлен:')
    print(char_poly)

    print()
    print()


    print('Интервалы собственных значений:')
    print(eigen_intervals)

    print()
    print()

    print('Собственные значения:')
    print(eigen_values)

    print()
    print()

    print('Собственные векторы Фробениуса:')
    print(frobenius_eigen_vectors)

    print()
    print()

    print('Собственные векторы:')
    print(eigen_vectors)

    print()
    print()

    print('Проверка на ортогональность:')
    print(check_ort(size_matrix, eigen_vectors, rtol=1e-2, atol=1e-2))
