num = int(input('enter a number between 1-10: '))

while num < 1 or num > 10:
    print(f"{num} the number is out of range!")
    num = int(input('enter a number between 1-10: '))
else:
    print(f'your number is {num}')