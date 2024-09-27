# membership operators = used to test whether a value  or variable is found in a sequence (string, list, tuple, set, or dictionary)
#       1. in 
#       2. not in 

# to see if a character is in the secret code
word = "APPLE"
letter = input("Guess a letter in the secret word: ")
if letter in word:
    print(f"There is a '{letter}' in the word")
else:
    print(f"{letter}' was not found")

# to see if a student is found
students = {"Spongebob", "Patrick", "Sandy"}
student = input("Enter the name of a student: ")
if student not in students: 
    print(f"{student} was not found")
else: 
    print(f"{student} is a student")

# using a dictionary to get grades of a student
grades = {"Shawn": "A", 
          "Lee": "A+", 
          "Shin": "C", 
          "Mori": "F"}

student = input("Enter the name of the student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else: 
    print(f"{student} was not found")

# seeing if "@" and "." are in an email to check validity
email = "slee1271@fake.ca"
if "@" in email and "." in email:
    print("Valid email")
else: 
    print("Invalid email")