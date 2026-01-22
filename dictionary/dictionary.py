# dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates

capitals = {'USA': 'Washington',
            'China': 'Beijing',
            'Indonesia': 'Jakarta',
            'Ukraine': 'Kyiv',
            'Russia': 'Moscow'}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Indonesia"))

# if capitals.get("Russia"):
#     print("the capital exists")
# else:
#     print("the capitals doesn't exists") 

# capitals.update({'Saudi': 'Jeddah'})
# capitals.update({'USA': 'New York'})
# capitals.pop("China")
# capitals.popitem()

# keys = capitals.keys()

# for keys in capitals.keys():
#     print(keys)

# for item in capitals.items():
#     print(item)

# for values in capitals.values():
#     print(values)

for key, value in capitals.items():
    print(f'{key}: {value}')