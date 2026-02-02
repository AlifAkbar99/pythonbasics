num_pad = [(1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#")]

print()
for row in num_pad:
    # print(row)
    for rows in row:
        print(rows, end=' ')
    print()
print()