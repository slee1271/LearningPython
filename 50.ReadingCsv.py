import csv

file_path = "FileReading/output47.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file) # give memory address
        for line in content:
            # print(line)
            print(line[0]) # gives all the names
except FileNotFoundError:
    print("That file was not found")
except PermissionError: # no permission to use file
    print("You do not have permission to read the file")