import math 

#circumference of a circle 
radius = float(input("Enter the radius of a circle in cm: "))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}cm") #rounds answer to 2 decimals

#area of a circle 
radius = float(input("Enter the radius of a circle in cm: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}cm^2")

#hypotenuse of right triangle 
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a,2) + pow(b,2))
print(f"The hypotenuse is {round(c,2)}")