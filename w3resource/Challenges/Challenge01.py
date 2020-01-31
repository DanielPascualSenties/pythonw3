def is_power_of_two(n):
    if n == 1:
        return True
    if n % 2:
        return False
    return is_power_of_two(int(n/2))


def is_power_of_three(n):
    if n == 1:
        return True
    if n % 3:
        return False
    return is_power_of_three(int(n/3))


def is_power_of_m(n, m):
    if n == 1:
        return True
    if n % m:
        return False
    return is_power_of_m(int(n/m),m)


print(is_power_of_m(27, 9))


