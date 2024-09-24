import random # gives us access to many new methods
# print(help(random)) # use this for help

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2","3","4","5","6","7","8","9","10","J","Q,","K","A"]

number = random.randint(low,high)
print(number)

float = random.random()
print(float)

option = random.choice(options)
print(option)

random.shuffle(cards)
print(cards)