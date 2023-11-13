import math

def calc_inaccuracy(x):
    values = [
        (x - 1) ** 6,
        (3 - 2 * x) ** 3,
        99 - 70 * x
    ]

    err = [
        6 / (math.sqrt(2) - 1) * abs(math.sqrt(2) - x),
        6 / (3 - 2 * math.sqrt(2)) * abs(math.sqrt(2) - x),
        70 / (99 - 70 * math.sqrt(2)) * abs(math.sqrt(2) - x)
    ]

    for i in range(len(err)):
        # print(values[i])
        print(err[i])

    print()
    corr_value = ((math.sqrt(2) - 1) / (math.sqrt(2) + 1)) ** 3
    print(corr_value)
    print()