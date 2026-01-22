menu = {'Pizza' : 3.00,
        'Rendang' : 2.45,
        'Dendeng' : 4.54,
        'Tunjang' : 5.00,
        'Rawon' : 3.45,
        'Croissant': 9.03,
        'Mandi' : 1.55,
        'Bakso' : 2.33,
        'Roti' : 3.22,
        'Burger' : 4.45,
        'Waffle' : 6.00}

cart = []
total = 0

print('------- MENU --------')
for key, value in menu.items():
    print(f'{key:10}: ${value:.2f}')
print('---------------------')

while True:
    food = input('Enter your menu (q to quit): ').lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print(cart)