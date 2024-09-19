# collection = single "variable" used to store multiple values
# List  = [] ordered and changeable. Duplicates OK [start:stop:step]
# Set   = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Faster

fruits = ["apple", "orange", "banana", "strawberry"]
print(fruits) #prints the list
print(fruits[2]) #prints banana but [4] would give an index error
print(fruits[::2]) 

print(len(fruits)) #find lengths
print("apple" in fruits) #gives bool
#print(dir(fruits)) #shows all possible methods
#print(help(fruits)) #give help

fruits[0] = "blueberry" #changes index 0 to blueberry so no longer apple
fruits.append("pineapple") #adds pineapple
fruits.remove("orange") #removes orange
fruits.insert(0, "blackberry")
fruits.sort() #alphabetical sort
fruits.reverse() #reverse the list 
#fruits.clear() #clears the list 
print(fruits.count("pineapple")) #counts the amount in the list
print(fruits) 
print(fruits.index("banana")) #what index location

fruits = {"apple", "orange", "banana", "strawberry"} #always prints in random order therefore we cant uses indexing [0]

fruits.add("coconut")
fruits.remove("apple")
fruits.pop() #removes the first element but always random
fruits.clear()
print(fruits)

fruits = ("apple", "orange", "banana", "strawberry", "banana")
print(fruits) 
print(fruits.index("apple"))
print(fruits.count("banana"))