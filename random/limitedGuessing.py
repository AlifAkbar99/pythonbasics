import random

lowest_num = 10
highest_num = 50
guesses = 0
is_running = True
number = random.randint(lowest_num, highest_num)

while is_running and guesses < 5:
    guess = input('Masukkan angka maksimal 5 percobaan: ')
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print('Angka diluar ambang batas silahkan coba lagi!')
        elif guess > number:
            print("Angkanya terlalu besar")
        elif guess < number:
            print('Angkanya terlalu kecil')
        else:
            print('Angkanya benar')
            break
    else:
        print('Invalid!')
        print('Inputan harus berupa angka!')

if guess != number:
    print(f'kamu kalah jawabannya adalah {number}')
        
print(f'Anda menebak sebanyak {guesses} percobaan')