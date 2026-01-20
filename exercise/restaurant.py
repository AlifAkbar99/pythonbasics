makanan = []
minuman = []
harga = []
total = 0
id_card = 0

print ('-------- WELCOME TO RESTAURANT ---------')
print()

name = input("masukkan nama anda: ")
print(f"baik {name}, sekarang anda konfirmasi apakah anda mempunyai id card atau tidak")

punya_id = input('apakah anda mempunyai id card? [y/n]: ')

while True:
    if punya_id.lower() == 'y':
        id_card = input('masukkan id card anda (12 digit): ')
        
        if id_card.isdigit() and len(id_card) == 12:
            print(f"{id_card}id card anda valid")
            break
        else:
            print("id card anda tidak valid")
    else:
        print("sampai jumpa")
        exit()

print('langkah selanjutnya pesan makanan dibawah ini: ')

while True:
    food = input('masukkan makanan yang mau anda beli [Q/q untuk keluar]: ')
    if food.lower() == 'q':
        break
    else:
        uang = float(input(f"masukkan berapa harga {food}: Rp."))
        makanan.append(food)
        harga.append(uang)
            
while True:
    beverage = input('masukkan minuman yang mau anda beli [Q/q untuk keluar]: ')
    if beverage.lower() == 'q':
        break
    else:
        uang_2 = float(input(f"masukkan berapa harga {beverage}: Rp."))
        minuman.append(beverage)
        harga.append(uang_2)

print()
print ('---- makanan dan minuman anda ----')
for food in makanan:
    print(food)
for beverage in minuman:
    print(beverage)
for price in harga:
    total += price
    
print()
print('---- TOTAL ----')
print(f'total anda sebanyak Rp.{total} ')
print(f'silahkan bayar melalui nomor: {id_card} anda melalui qr yang telah disediakan')
print('terimakasih')
print()