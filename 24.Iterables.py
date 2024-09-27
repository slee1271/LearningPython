# iterables is an object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

numbers = [1,2,3,4,5]
for number in numbers:
    print(number, end=" ")
print()

fruits = {"apple", "orange", "banana", "coconut"}
for fruit in fruits:
    print(fruit)

name = "Shawn Lee"
for character in name:
    print(character, end="-")
print()

dictionary = {"A": 1, "B": 2, "C": 3}
for key in dictionary:
    print(key, end=" ")
print("Keys")

for value in dictionary.values():
    print(value, end= " ")
print("Values")

for key, value in dictionary.items():
    print(f"{key}: {value}")
print("Keys: Values")