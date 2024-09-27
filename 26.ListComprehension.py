# list comprehension = a consise way to create lists in python 
#                       compact and easier to read than traditional loops
#                       [expression for value in iterable if condition]

doubles = []

for x in range(1,11):
    doubles.append(x * 2)
print(doubles)

doubles = [x*2 for x in range(1,11)] # written in one line
print(doubles)
triples = [y*3 for y in range(1,11)]
print(triples)
squares = [z*z for z in range(1,11)]
print(squares)

fruits = ["apple", "orange", "banana", "strawberry"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

numbers = [1,-2,3,-4,5,-6,-7,8]
positive_nums = [num for num in numbers if num>=0]
print(positive_nums)
negative_nums = [num for num in numbers if num<=0]
print(negative_nums)
odd_nums = [num for num in numbers if num%2==1]
print(odd_nums)
even_nums = [num for num in numbers if num%2==0]
print(even_nums)

grades = [85,42,79,90,56,61,30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)