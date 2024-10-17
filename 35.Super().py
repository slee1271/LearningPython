# super() = function used in a child class (subclass) to call methods from a parent class (superclass)
# allows you to extend the functionality of the inherited methods


# this class is created bc circle, square, triangle all share colour and filled
class Shape:
    def __init__(self, colour, filled):
        self.colour = colour
        self.filled = filled
    
    def describe(self):
        print(f"It is {self.colour} and {"filled" if self.filled else "not filled"}")

class Circle(Shape):
    def __init__(self, colour, filled, radius):
        # self.colour = colour
        # self.filled = filled
        super().__init__(colour,filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius**2}")
        super().describe()


class Square(Shape):
    def __init__(self, colour, filled, width):
        super().__init__(colour,filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, colour, filled, width, height):
        super().__init__(colour,filled)
        self.width = width
        self.height = height

circle = Circle("red", True, 5)
print(circle.colour)
print(circle.filled)
print(circle.radius)

# the describe() of circle will be called instead of the parent describe of Shape
circle.describe()
print()

triangle = Triangle("yellow", False, 4, 8)
print(triangle.colour)
print(triangle.filled)
print(triangle.width)
print(triangle.height)
triangle.describe()
