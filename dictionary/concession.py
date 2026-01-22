menu = {'pizza' : 3.00,
        'rendang' : 2.45,
        'dendeng' : 4.54,
        'tunjang' : 5.00,
        'rawon' : 3.45,
        'croissant': 9.03,
        'mandi' : 1.55,
        'bakso' : 2.33,
        'roti' : 3.22,
        'burger' : 4.45,
        'waffle' : 6.00}

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
print('---------------------')
for food in cart:
    total += menu.get(food)
    print(food, end=' ')

print()
print(f'Total is: ${total:.2f}')