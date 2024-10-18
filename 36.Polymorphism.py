# Polymorphism is a greek word which means "have many forms or faces"
# Two ways to achieve polymorphism
    # Inheritance = an object that could be treated of the same type as a parent class
    #"Duck typing" = object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base 
        self.height = height
    def area(self):
        return self.base * self.height / 2

#Pizza is considered a Pizza, a Circle, and a Shape
class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni", 15)]

for shape in shapes:
    print(shape.area())