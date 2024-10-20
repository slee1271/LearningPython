file_path = "FileReading/output45.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError: # no permission to use file
    print("You do not have permission to read the file")