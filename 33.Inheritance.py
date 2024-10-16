# inheritance allows a class to inherit attributes and methods from another class
# helps with code reusability and extensibility 

# Creating an animal class where other animals will inherit attributes and methods from the animal class  

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

# we dont need to copy line 7-15 in dog, cat, mouse class
class Dog(Animal):
    def speak(self):
        print("woof")
     

class Cat(Animal):
    def speak(self):
        print("meow")

class Mouse(Animal):
    def speak(self):
        print("squeak")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

dog.speak()
cat.speak()
mouse.speak()