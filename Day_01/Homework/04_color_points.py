from math import sqrt


class Point:
    def __init__(self, x, y, color="red"):
        self.x = x
        self.y = y
        self.color = color

    def distance(self, other_point) -> float:
        """ Расстояние между двумя точками """
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# пример работы метода
# p1 = Point(4, 4)
# p2 = Point(3, 3)

# result = p1.distance(p2)
# print(result)


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно, что точек каждого цвета ровно три, но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]
# Все точки одного цвета соединены линиями и образуют треугольник

# Задание-1: доработайте конструктор class Point для хранения цвета точки
# Задание-2: реализуйте метод distance()
# Задание-3: вычислите площади треугольников образованных из точек одного цвета(зеленый и красный)
# для вычисления площади можно использовать формулу Герона:
# math.sqrt(p * (p-a) * (p-b) * (p-c)), где p - это полупериметр

# TODO: your code here...


def get_triangle_area(a, b, c):
    p = sum([a, b, c]) / 2
    return sqrt(p * (p-a) * (p-b) * (p-c))


list_of_red = [x for x in points if x.color == 'red']
list_of_green = [x for x in points if x.color == 'green']

red_a, red_b, red_c = (
    list_of_red[0].distance(list_of_red[1]),
    list_of_red[1].distance(list_of_red[2]),
    list_of_red[2].distance(list_of_red[0])
)

green_a, green_b, green_c = (
    list_of_green[0].distance(list_of_green[1]),
    list_of_green[1].distance(list_of_green[2]),
    list_of_green[2].distance(list_of_green[0])
)


print(f"Площадь красного треугольника = {get_triangle_area(red_a, red_b, red_c)}")
print(f"Площадь зеленого треугольника = {get_triangle_area(green_a, green_b, green_c)}")
