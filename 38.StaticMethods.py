# static methods = a method that belongs to a class rather than any object from that class (instance)
# instance methods = best for operations on instances of the class (object)
# static methods = best for utility. functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name 
        self.position = position

    # instance method
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    # static method
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cook", "Cashier", "Janitor"]
        return position in valid_positions 
    
print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Scientist"))

employee1 = Employee("Shawn", "Manager")
employee2 = Employee("Lee", "Cashier")

print(employee1.get_info())
print(employee2.get_info())
