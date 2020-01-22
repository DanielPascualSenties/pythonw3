
double = lambda x: x * 2
square = lambda x: x * x
cube = lambda x: x * x * x


def apply_to_list(x):
    z = map(double, x)
    return z


y = apply_to_list([1, 2, 3, 4])
print(y)
