class Vector:
    def __init__(self, value):
        self.value = value

    def size(self):
        return len(self.value)

    def __mul__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Передается не вектор")

        if self.size() != other.size():
            raise ValueError("Вектора разной размерности")

        result = sum(x * y for x, y in zip(self.value, other.value))

        return result

    def normalize(self):
        square_sum = sum([x ** 2 for x in self.value])
        return square_sum ** 0.5
