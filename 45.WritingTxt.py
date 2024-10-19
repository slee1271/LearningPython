txt_data = "Hello World!"
employees = ["Shawn", "Shin", "Mori", "Lee"]

file_path = "FileReading/output45.txt"
file_path2 = "FileReading/outputList45.txt"


# "w" is write and will overwrite file, "x" will write if files DNE but will give error if it already exists(FileExistsError), "a" is to append(adding) to the file, "r" is for read
try:
    with open(file_path, "a") as file:
        file.write(txt_data + "\n")
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("That file already exists")

try:
    with open(file_path2, "w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file {file_path2} was created")
except FileExistsError:
    print("That file already exists")