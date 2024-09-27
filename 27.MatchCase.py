# match-case statement (aka switch in other languages): an alternative to using many "elif" statements.
# executes code if a value matches a 'case'. cleaner and syntax is more readable 

"""
def day_of_week(day):
    if day == 1:
        return "Today is Sunday"
    elif day == 2:
        return "Today is Monday"
    elif day == 3:
        return "Today is Tuesday"
    elif day == 4:
        return "Today is Wednesday"
    elif day == 5:
        return "Today is Thursday"
    elif day == 6:
        return "Today is Friday"
    elif day == 7:
        return "Today is Saturday"
    else:
        return "Not a valid day"
"""

# change to 
def day_of_week(day):
    match day:
        case 1:
            return "Today is Sunday"
        case 2:
            return "Today is Monday"
        case 3:
            return "Today is Tuesday"
        case 4:
            return "Today is Wednesday"
        case 5:
            return "Today is Thursday"
        case 6:
            return "Today is Friday"
        case 7:
            return "Today is Saturday"
        case _:
            return "Not a valid day"

print(day_of_week(1))
print(day_of_week(7))
print(day_of_week("pizza"))
print()

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday": # "|" is the or operator
            return True
        case _:
            return False

print(is_weekend("Sunday"))
print(is_weekend("Saturday"))
print(is_weekend("Monday"))
print(is_weekend("pizza"))

