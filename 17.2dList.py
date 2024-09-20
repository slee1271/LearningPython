fruits = ["apple", "orange", "banana", "strawberry"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "beef", "fish"]

groceries = [fruits, vegetables, meats]
print(groceries)
print(groceries[0]) # prints fruits list
print(groceries[0][0]) # prints apple

for collection in groceries:
    for food in collection:
        print(food) # (food, end=" ") to make it grid like
    print()
