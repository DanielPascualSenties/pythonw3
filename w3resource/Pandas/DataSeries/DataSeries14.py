import pandas

s = pandas.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(s)

f = s.reindex([0, 2, 1, 3, 4, 5, 7, 6, 8, 9, 10])
print(f)
