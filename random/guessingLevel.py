import random

number = 1
level_1 = random.randint(number, 10)
level_2 = random.randint(number, 50)
level_3 = random.randint(number, 100)
guesses = 0
is_running = True

while is_running:
    guess = input('masukkan angka pada level 1: ')
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < number or guess > 10:
            print('angka di luar ambang batas coba lagi!')
        elif guess < level_1:
            print('angka terlalu rendah')
        elif guess > level_1:
            print('angka terlalu tinggi')
        else:
            print('Jawaban benar')
            print('selanjutnya anda ke level 2!')
            break
    else:
        print('invalid')
        print('Anda tidak memasukkan angka! coba lagi')
    
while is_running:
    guess = input('masukkan angka pada level 2: ')
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
            
        if guess < number or guess > 50:
            print('angka di luar ambang batas coba lagi!')
        elif guess < level_2:
            print('angka terlalu rendah')
        elif guess > level_2:
            print('angka terlalu tinggi')
        else:
            print('jawaban benar')     
            print('Selanjutnya anda ke level 3!')
            break
    else:
        print('invalid')
        print('Anda tidak memasukkan angka! coba lagi')

while is_running:
    guess = input('masukkan angka pada level 3: ')
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < number or guess > 100:
            print('angka di luar ambang batas! coba lagi')
        elif guess < level_3:
            print('angka terlalu rendah')
        elif guess > level_3:
            print('angka terlalu tinggi')
        else:
            print('jawaban benar')
            print('Selamat! anda berhasil menamatkan permainan ini')
            break

print('----------------- SCORE ------------------')
print(f'anda berhasil menebak sebanyak {guesses} percobaan')
