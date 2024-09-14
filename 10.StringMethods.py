name = input("Enter your full name: ")

print(len(name)) # gives length of string
print(name.find(" ")) #shows where the space is. index starts at 0 (shawn lee would give "5" 0,1,2,3,4,5)

result = name.find("e") #can write .find(" ", start, stop) but default it searches the whole string
print(result)
result = name.rfind("e") # .rfind finds for string in reverse to find the last occurence
print(result)
result = name.find("q") # python will give -1 if the letter cannot be found 
print(result)

name = name.capitalize() # capitalize the first letter only
print(name)
name = name.upper() # all capital letters
print(name)
name = name.lower() # all lower case letters
print(name)

name = name.isdigit() #the whole string needs to be digits (123 = True, Shawn123 = False)
print(name)

# for some reason name.isalpha only works if name.isdigit is commented 
name = name.isalpha() #True if string contains only alphabetical characters. space will give false 
print(name)


phone_number = input("Enter your phone number: ")
result = phone_number.count("-")
print(result)

result = phone_number.replace("-", " ") # replaces the first arg in the bracket with the 2nd arg 
print(result)

print(help(str)) # for other basic string methods then :q to quit or type h for help then q to quit
