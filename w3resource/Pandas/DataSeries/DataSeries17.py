import pandas



s1 = pandas.Series([1, 2, 3, 4, 5])
s2 = pandas.Series([2, 4, 6, 8, 10])

union = s1.append(s2)
inters = s1[s1.isin(s2)]
res = union[~union.isin(inters)]
print(res)

