# exception = an event that interrupts the flow of a program 
# ZeroDivisionError = dividing by zero 
# TyperError = 1 + "1"
# ValueError = int("string")

# 1.try -> 2.except -> 3.finally
#good practice to use try,except,finally for user input because they can enter anything which is dangerous

#user input types 0
try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide be zero")
except ValueError:
    print("You can enter only numbers")

# will catch all exceptions but is bad practice bc it doesn't tell us the error
except Exception:
    print("Something went wrong")

# this will always run
finally:
    print("Some clean up like closing files")