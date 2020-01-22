tup = (1, 3, "banana", 5, [1, 3], 3, 12)
singles = []
repeated = []
for i in range(len(tup)):
    if tup[i] in singles:
        repeated.append(tup[i])
    else:
        singles.append(tup[i])

print(singles)
print(repeated)
