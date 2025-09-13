class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rect(width:{self.width}, height:{self.height})'

    def __str__(self):
        return f'Value width is {self.width}, value height in {self.height}'

    def __mul__(self, other):
        try:
            if isinstance(other, (int, float)):
                self.width *= other
                self.height *= other
        except:
            ValueError

    def get_area(self):
        return self.width * self.height

    def __lt__(self, other):
        return self.get_area() < Rect.get_area(other)

    def __gt__(self, other):
        return self.get_area() > Rect.get_area(other)

    def __le__(self, other):
        return self.get_area() <= Rect.get_area(other)

    def __ge__(self, other):
        return self.get_area() >= Rect.get_area(other)

    def __eq__(self, other):
        return self.get_area() == Rect.get_area(other)

    def __ne__(self, other):
        return self.get_area() != Rect.get_area(other)


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
