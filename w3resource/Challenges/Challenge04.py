import math


def is_perfect_square(n):
    root = int(math.sqrt(n))
    return root*root == n


print(is_perfect_square(9))
