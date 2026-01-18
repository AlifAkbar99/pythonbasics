age = int(input('enter your age: '))
while age < 0:
    print("age cannot be negative!")
    age = int(input('enter your age: '))
else:
    print(f'youf age {age} years old')