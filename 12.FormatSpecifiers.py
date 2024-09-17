# format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 3.1415
price2 = -987.65
price3 = 12.34

print(f"Price 1 is: ${price1:.2f}") # format to two decimal places
print(f"Price 2 is: ${price2:10}") # has a total of 10 spaces ({:010} to add 0 instead of ws)
print(f"Price 3 is: ${price3:<10}") # move to far left of the 10 spaces
print(f"Price 3 is: ${price3:>10}") # move to far right of the 10 spaces
print(f"Price 3 is: ${price3:^10}") # move to center of the 10 spaces
print(f"Price 1 is: ${price1:+}") # only displays + for all positive numbers

print(f"Price 1 is: ${price1: }") # add space to give space to show for positive or negative number 
print(f"Price 2 is: ${price2: }") 

price4 = 123456.7890
print(f"Price 4 is: ${price4:,}") # seperates 1,000 with comma
print(f"Price 4 is: ${price4:+,.2f}") # can mix and match format specifiers