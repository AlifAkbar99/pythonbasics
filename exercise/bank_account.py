import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

print('---------------------')
print('Welcome to the bank account')
print('---------------------')
print(' ')

name = input('Enter your name: ')
print(f'your name is {name}') 

while True:
    age = int(input('Enter your age: '))
    id_card = (input('input your id card: '))
    
    if id_card.isdigit() and len(id_card) == 12 and age >= 18:
        print(f'\nyour {id_card} and {age} are valid')
        break
    
    elif age < 18:
        print('you are under 18. you cannot create an acoount')
        
    elif id_card != len(id_card) == 12:
        print('Your ID must be exactly 12 digits')
    else:
        print('registraition is failed')

print('Next step: register your account')
print(' ')