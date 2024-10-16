# Object is a "bundle" of related attributes (variables)n and methods (funtions)
# Class is a blueprint used to design the structure and layout of an object 

from car31 import Car

car1 = Car("Supra", 2024, "red", False)

print(car1.model) 
print(car1.year)
print(car1.colour)
print(f"For sale: {car1.for_sale}")

car1.drive()
car1.stop()

car1.describe()