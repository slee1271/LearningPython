# for loops execute a block a code a fixed number of time. You can iterate over a range, string, sequence, etc
# for x in range (inclusive, exclusive, step)

for x in reversed(range(0,11)): # counts backwords
    print(x)
print("Happy New Year")

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)

for x in range (1,20):
    if x == 13: # skips 13 bc its an unlucky number
        continue # if you use break the code will stop at 12
    else: 
        print(x)