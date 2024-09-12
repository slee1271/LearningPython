#area of rectangle 
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
print(f"The area is {area} units^2")

#shopping cart 
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input(f"How many {item}/s are you buying?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")