import pandas

s = pandas.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])
print(s)

n = s.apply(pandas.Series).stack().reset_index(drop=True)
print(n)

