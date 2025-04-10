import math
from abc import ABC, abstractmethod


class Volume(ABC):

    @abstractmethod
    def volume(self):
        pass


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Cube(Shape, Volume):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 6 * (self.side ** 2)

    def volume(self):
        return self.side ** 3


class Cylinder(Shape, Volume):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        return (2 * math.pi * self.radius ** 2) + (2 * math.pi * self.radius * self.height)

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height
