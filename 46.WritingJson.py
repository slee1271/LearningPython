import json

employee = {"name": "Shawn",
            "age": 50,
            "Job": "Coder"}

file_path = "FileReading/output46.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file {file_path} was created")
except FileExistsError:
    print("That file already exists")