password: 12345
username = 'admin'

while True:
    user_name = input('masukkan username: ')
    
    if username == user_name:
        print("langkah selanjutnya, masukkan password anda")
        password = 12345
        pass_word = int(input('masukkan password: '))
        if password == pass_word:
            print('anda berhasil login')
            break
        else:
            print("password anda salah, coba lagi")
    else:
        print("username anda salah, coba lagi")
    