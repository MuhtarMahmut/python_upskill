from abc import ABC, abstractmethod


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
        print("Calculating the area of Square")


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Calculating the area of Circle")


class Cube(Shape):
    pass


class Cylinder(Shape):
    pass




