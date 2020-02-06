import pandas


d = {'a':100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
print(d)
print(type(d))

dsd = pandas.Series(d)
print(dsd)
print(type(dsd))
