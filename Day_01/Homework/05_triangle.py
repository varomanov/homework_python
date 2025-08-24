from typing import Self
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point: Self) -> float:
        """ Расстояние между двумя точками """
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimeter(self):
        a, b, c = (
            self.p1.distance(self.p2),
            self.p2.distance(self.p3),
            self.p3.distance(self.p1)
        )
        return sum([a, b, c])

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        a, b, c = (
            self.p1.distance(self.p2),
            self.p2.distance(self.p3),
            self.p3.distance(self.p1)
        )
        p = sum([a, b, c]) / 2
        return sqrt(p * (p-a) * (p-b) * (p-c))


# Треугольник задан координатами трех точек
triangle = Triangle(Point(2, 4), Point(6, 8), Point(8, 0))

# Задание:
# найдите площадь и периметр треугольника, реализовав методы area() и perimeter()

print(f"Периметр треугольника = {triangle.perimeter():.2f}")
print(f"Площадь треугольника = {triangle.area():.2f}")
