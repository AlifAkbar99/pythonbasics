import random

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f'enter a number between ({low} - {high}): '))
    
    # mengambil nilai untuk guesses paling bawah
    guesses += 1
    
    if guess < number:
        print(f'{guess} is too low')
    elif guess > number:
        print(f'{guess} is to high')
    else:
        print(f'{guess} is correct!')
        break

# guesses: akan menghitung jumlah berapa banyak tebakan seperti guesses += 1
print(f'this round took you {guesses} guesses')