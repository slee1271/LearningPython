# accessing elements of a sequence using [] [start(inclusive) : stop(exclusive) : end]
card_num = "1234-5678-9012-3456"
print(card_num[0])
print(card_num[0:4])
print(card_num[:4]) # same as line above
print(card_num[5:9])
print(card_num[5:]) # need the last 12 digits of card num
print(card_num[-1]) # goes backwards
print(card_num[::2]) # prints every second number
print(card_num[::-1]) # backwards

last_digits = card_num[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")