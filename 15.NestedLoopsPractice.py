row = int(input("Enter the # of rows: "))
column = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use")

for x in range(row):
    for y in range(column):
        print(symbol, end="")
    print()

