import pandas


def divide_series(s1, s2):
    return int(s1 / s2)


s = pandas.Series([51, 27, 34, 48, 15])
e = pandas.Series([49, 73, 66, 52, 85])


su = divide_series(s,e)
print(su)

# TODO no funciona