import pandas

s = pandas.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(s)

f = s[s < 7]
print(f)