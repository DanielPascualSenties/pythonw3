def is_prime(n):
    if n == 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(7))
print(is_prime(8))
