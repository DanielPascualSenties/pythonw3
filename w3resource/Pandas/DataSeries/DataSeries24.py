import pandas


def make_great(x):
    return x[0].upper() + x[1:-1] + x[-1].upper()


s = pandas.Series(['php', 'python', 'java', 'c++', 'haskell', 'prolog', 'minizinc', 'vba', 'html', 'css', 'javascript'])
print(s)
res = s.map(lambda x: make_great(x))
print(res)


