from abstractions2 import Square, Circle, Cube, Cylinder, Shape

square: Square = Square(2.5)
circle: Circle = Circle(3.5)
cube: Cube = Cube(4.5)
cylinder: Cylinder = Cylinder(2.5, 5.5)

print("-----------------")

shape: Shape = Cylinder(2.5, 5.5)
print(shape)

print("-----------------")


def display_area(sh: Shape):
    print(f"The area of the {type(sh).__name__} is {sh.area()}")


display_area(shape)

print("-----------------")

shapes = [Square(2.5), Circle(3.5), Cube(4.5), Cylinder(2.5, 5.5)]

for each_shape in shapes:
   display_area(each_shape)

