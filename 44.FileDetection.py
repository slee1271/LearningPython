import os 

file_path = "test44.txt" 

# for files in folders
file_path = "FileReading/test44.txt"


if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory/folder")
else:
    print("The location doesn't exist")