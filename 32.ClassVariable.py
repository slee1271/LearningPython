# class variable is shared among all instances/objects of a class
# defined outside the constructor 
# allows you to share data among al objects created from that class

class Student:

    # class variable
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age =  age
        Student.num_students += 1 #increments counter for num of students

student1 = Student("John", 20)
student2 = Student("Bob", 25)
student2 = Student("Ty", 27)


print(student1.name)
print(student1.age)

print(student1.class_year) # bad practice
print(Student.class_year) # do this instead
print(Student.num_students) # number of students initialized

print(f"Class of {Student.class_year} has {Student.num_students} students")