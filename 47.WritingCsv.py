import csv

employee = [["Name", "Age", "Job"],
            ["Shawn", 20, "Coder"],
            ["Lee", 25, "Cook"],
            ["Shin", 30, "Cleaner"]]

file_path = "FileReading/output47.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employee:
            writer.writerow(row)
        print(f"csv file {file_path} was created")
except FileExistsError:
    print("That file already exists")