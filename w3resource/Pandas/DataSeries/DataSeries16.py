import pandas



s1 = pandas.Series([1, 2, 3, 4, 5])
s2 = pandas.Series([4, 5, 6, 7, 8])

res = s1[~s1.isin(s2)]
print(res)
