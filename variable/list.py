# [] list = ordered and changeable. Duplicates ok

print('')
print('------LIST-------')
print(' ')
fruits = ['apple', 'banana', 'orange', 'salak', 'durian']
print(fruits)
print(' ')
print('to show the list: ')
for fruit in fruits:
    print(fruit)
print('')
print('to show how much length of the list:')
print(len(fruits))
print('')

print('to show one variable')
print(fruits[0])
print(fruits[3])
print(fruits[::2])
print('')

print('reverse of the list')
print(fruits[::-1])
print('')

print('changes variable apple to pineapple: ')
fruits[0] = 'pineapple'
for buah in fruits:
    print(buah)
print('')

print('add lemon to the list: ')
fruits.append('lemon')
print(fruits)
print('')

print('remove banana from the list: ')
fruits.remove("banana")
print(fruits)
print('')

print('add rambutan beetwen salak and durian: ')
fruits.insert(3, 'rambutan')
print(fruits)
print('')

print('sorting and reverse the list: ')
fruits.sort()
reverse = fruits
print(fruits)
reverse.reverse()
print(reverse)
print('')

print('counting variable: ')
print(fruits.count("orange"))

print('')
print('another function: ')
print(dir(fruits))
# print(help(fruits))