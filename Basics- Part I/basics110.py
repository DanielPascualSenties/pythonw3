lis = [1, 3, 15, 26, 30, 37, 45, 56, ]

divisibles = list(filter(lambda x: (x % 15 == 0), lis))

print(divisibles)
