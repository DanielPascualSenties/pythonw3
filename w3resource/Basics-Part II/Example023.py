def sum_of_digits(num):
    if num < 10:
        return num
    units = num % 10
    rest = int(num /10)
    return units + sum_of_digits(rest)


print(str(sum_of_digits(26234234)))