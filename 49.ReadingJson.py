import json

file_path = "FileReading/output46.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
        print(content["name"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError: # no permission to use file
    print("You do not have permission to read the file")