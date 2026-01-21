fruits = ['grape', 'coconut', 'apple', 'banana']
meats = ['raw', 'beef', 'pork']
properties = ['chair', 'table', 'window']

things = [fruits, meats, properties]

print()
print(things)
print()

print(things[0])
print()

print(things[0][2])
print()

fruits[0] = 'pear'
print(things)
print()

for collection in things:
    print(collection)
print()

for collection in things:
    for food in collection:
        print(food, end=' ')
    print()
print()