foods = []
prices = []
total = 0

while True:
    food = input('Enter a food to buy (q or quit): ')
    if food.lower() == 'q':
        break
    else:
        price = float(input(f'enter the price of a {food}: Rp.'))
        foods.append(food)
        prices.append(price)

print('------- Your Cart --------')

for food in foods:
    print(food, end=' ')
    
for price in prices:
    total += price

print()
print(f'your total is: {total}')