def max_2(a, b):
    if a > b:
        return a
    else:
        return b


def max_3(a, b, c):
    x = max_2(a, b)
    return max_2(x, c)
