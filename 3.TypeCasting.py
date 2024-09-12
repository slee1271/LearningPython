# typecasting is the process of converting a variable from one data type to another

name = "Shawn"
age = 22 
gpa = 3.98 
is_student = True

print(type(name)) #type() give the type of the variable

gpa = int(gpa) #truncates the decimals
print(gpa)

age = str(age) #changes to string so cannot use arithmetic but still looks the same
print(age)
print(type(age))

age = float(age) #gives decimal to int
print(age)


#adding nums and strings 
age2 = 18 
age2 = age2 + 1
print(age2) #gives 19

age2 = str(age2)
age2 = age2 + "1"
print(age2) #gives 191

name = bool(name)
print(name) #will always give true as long as it isn't empty 