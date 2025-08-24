class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point) -> float:
    """ Расстояние между двумя точками """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


# Дан список точек
points = [
    Point(2, 7),
    Point(12, 7),
    Point(5, -2),
    Point(10, -16),
    Point(-12, 0)
]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
# TODO: your code here...

lst_todict = {points[i]: distance(Point(0, 0), points[i]) for i in range(len(points))}

for key, value in lst_todict.items():
    if value == max(lst_todict.values()):
        result = f'Координаты наиболее удаленной точки = (x={key.x}, y={key.y})'

print(result)
