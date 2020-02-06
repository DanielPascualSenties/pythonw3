import pandas

s = pandas.Series(['200', 'python', '300.12', '400'])
print(s)

t = s.append(pandas.Series(['500', 'php'])).reset_index(drop=True)
print(t)
