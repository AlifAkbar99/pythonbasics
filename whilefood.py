food = input('Enter a food would you like (q or quit): ')

while not food == 'q' and not food == 'quit':
    print(f'you like {food}!')
    food = input('Enter a food would you like (q or quit): ')
else:
    print('oke fair enough!')