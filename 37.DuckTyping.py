# "Duck typing" = Another way to acheive polymorphism besides inheritance. Object must have the minimum necessary attributes/methods

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")

class Car:
    def speak(self):
        print("honk")
    alive = False

animals = [Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)