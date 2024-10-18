# @Property = decorator used to define a method as a property (it can be accessed like an attribute)
# Benefits: add additional logic when read, write, or delete attributes. Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width # _width is private variable
        self._height = height # _height is a private variable

    #getter methods for width and height
    @property
    def width(self):
        return f"{self._width:.1f}cm" 

    @property
    def height(self):
        return f"{self._height:.1f}cm" 

    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater then zero")

    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._width = new_height
        else:
            print("Height must be greater then zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Width has been deleted")

rectangle = Rectangle(3,4)
print(rectangle._width)
print(rectangle._height)
print(rectangle.width)
print(rectangle.height)

rectangle.width = 5
rectangle.height = -1

del rectangle.width
del rectangle.height

