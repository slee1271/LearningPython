# dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates

capitals = {"USA": "Washington",
            "India": "New Delhi",
            "China": "Beijing", 
            "Russia": "Moscow"}

print(capitals.get("USA"))
print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"}) # adds to dictionary 
capitals.update({"USA": "New York"}) # updates USA in the dictionary 
capitals.pop("China") # removes China
capitals.popitem() # will remove the key and value in the very back
# capitals.clear() #clears dictionary
print(capitals)

keys = capitals.keys() 
for key in capitals.keys(): #use for loop to iterate over keys
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
print(items) #returns something similar to 2D tuples
for key, value in capitals.items():
    print(f"{key}: {value}")
