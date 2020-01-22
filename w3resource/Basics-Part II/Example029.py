def intersection(l1, l2):
    res = [v for v in l1 if v in l2]
    return res


def divide_into_primes(num, base=2, seq=None):
    if seq is None:
        seq = []
    if num == 1:
        return seq
    for i in range(base, num+1):
        if not num % i:
            seq.append(i)
            return divide_into_primes(int(num/i), i, seq)


x = divide_into_primes(2340)
print(x)
y = divide_into_primes(11230)
print(y)

common = intersection(x, y)
print(common)

# TODO there are issues with repeated elements