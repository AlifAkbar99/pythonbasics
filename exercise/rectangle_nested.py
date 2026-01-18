rows = (int(input("enter your number: ")))
columns = (int(input("enter your number: ")))
symbols = (input("enter your symbol: "))

for x in range (rows):
    for y in range (columns):
        print(symbols, end="")
    print()