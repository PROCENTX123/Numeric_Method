import math
import random


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

        return Vector(result)

    def normalize(self):
        square_sum = sum([x ** 2 for x in self.value])
        return math.sqrt(square_sum)


    def sub(self, other):
        if self.size() != other.size():
            raise ValueError("Вектора разной размерности")
        result = []
        for i in range(self.size()):
            result.append(self.value[i] - other.value[i])
        return Vector(result)

    @classmethod
    def fill_random(cls, n):
        values = [random.random() for _ in range(n)]
        return cls(values)
