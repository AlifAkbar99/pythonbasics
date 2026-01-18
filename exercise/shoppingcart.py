item = input("what item would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("how many items would you like to buy?: "))

total = price * quantity

print(f'you have bought {quantity} x {item}/s')
print(f'your total is: Rp{total}')