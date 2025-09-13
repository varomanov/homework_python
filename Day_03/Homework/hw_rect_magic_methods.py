class Rect:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rect({self.width}, {self.height})'

    def __str__(self):
        return f'Value width is {self.width}, value height in {self.height}'

    def __mul__(self, other: int | float):
        try:
            if isinstance(other, (int, float)):
                self.width *= other
                self.height *= other
        except:
            TypeError('Bad Type')

    def get_area(self):
        return self.width * self.height

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()


r1 = Rect(2, 23)
r2 = Rect(23, 10)
r1 * 5
print(r1)
print(r1 < r2)
print(r1 > r2)
print(r1 <= r2)
print(r1 >= r2)
print(r1 == r2)
print(r1 != r2)
