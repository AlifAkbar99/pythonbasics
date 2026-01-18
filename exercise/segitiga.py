for x in range (1, 7):
    print("*" * x)
    
print(' ')

for i in range (1, 6):
    for j in range (i):
        print("*", end="")
    print()

print(' ')

for i in range (5, 0, -1):
    for j in range (i):
        print("*", end="")
    print()