import math

a = float(input("Enter a side A: "))
b = float(input('Enter a side B: '))

c = math.sqrt (pow(a, 2) + pow(b, 2))

print (f"the result is {c} cm")
print (f'the result is {round(c, 2)} cm')