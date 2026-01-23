import random

guesses = 0
number = 1

for level in range(1, 4):

    if level == 1:
        max_num = 10
    elif level == 2:
        max_num = 50
    else:
        max_num = 100

    secret = random.randint(number, max_num)

    print(f'Level yang kamu dapat {level}')
    print(f'Tebak angka antara {number} sampai {max_num}')

    while True:
        guess = input('Masukkan angka: ')
        
        if not guess.isdigit():
            print('input harus angka!')
            continue
        guess = int(guess)
        guesses += 1
        
        if guess < number or guess > max_num:
            print('Diluar batas cik')
        elif guess < secret:
            print('Terlalu kecil')
        elif guess > secret:
            print('Terlalu besar')
        else:
            print('BENAR')
            break

print()
print('Selamat anda dapat pantat mas gatot 🎉')
print(f'jumlah percobaan anda sebanyak: {guesses}')