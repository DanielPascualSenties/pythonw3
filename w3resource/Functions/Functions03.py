def multiply_list(a):
    total = 1
    for i in a:
        total *= i
    return total


t = multiply_list([1, 5, 14])
print(t)
