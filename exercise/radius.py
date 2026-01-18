import math

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)


print(f'the result of cicumference is {round(circumference, 2)} cm')
print(f'the result of area is {round(area, 2)} cm^2')