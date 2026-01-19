takjil = []
harga = []
total = 0

while True:
    food = input('Masukkan takjil yang anda mau (tekan q atau Q untuk keluar): ')
    if food.lower() == 'q':
        break
    else:
        uang = float(input(f'masukkan harga {food}: Rp.'))
        takjil.append(food)
        harga.append(uang)

for food in takjil:
    print(food, end=' ')

for uang in harga:
    total += uang

print()
print(f'anda harus membayar sebesar {total}: ')
