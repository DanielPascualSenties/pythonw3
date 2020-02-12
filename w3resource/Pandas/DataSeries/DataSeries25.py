import pandas

s = pandas.Series(['php', 'python', 'java', 'c++', 'haskell'])

print(s)

res = s.map(lambda x: len(x))
print(res)