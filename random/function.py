import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A", "Joker" ]

print()
print('------- RANDOM -------')
number = random.randint(low, high)
print(number)

print('----------------------')
number = random.random()
print(number)

print('----------------------')
option = random.choice(options)
print(option)

print('----------------------')
random.shuffle(cards)
print(cards)