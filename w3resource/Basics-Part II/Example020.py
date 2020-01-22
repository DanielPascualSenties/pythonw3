# Solución a lo bruto
def number_of_zeroes(num, zeroes=0):
    if num%10:
        return zeroes
    else:
        return number_of_zeroes(num/10, zeroes+1)


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)


x = number_of_zeroes(factorial(21))
print(str(x))


# Solución astuta
def number_of_zeroes_v2(num):
    return int(num/5)


z = number_of_zeroes_v2(21)
print(str(z))

