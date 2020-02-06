import pandas


def add_series(s1, s2):
    return s1 + s2


def substract_series(s1, s2):
    return s1 - s2


def multiply_series(s1, s2):
    return s1 * s2


def divide_series(s1, s2):
    return s1 / s2


s = pandas.Series([51, 27, 34, 48, 15])
e = pandas.Series([49, 73, 66, 52, 85])

su = add_series(s,e)
print(su)
su = substract_series(s,e)
print(su)
su = multiply_series(s,e)
print(su)
su = divide_series(s,e)
print(su)

