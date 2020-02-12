import pandas


def contains_two_vowels(x):
    count = 0
    for i in x:
        if i in ['a', 'e', 'i', 'o', 'u']:
            count += 1
            if count > 1: return True
    return False


s = pandas.Series(['php', 'python', 'java', 'c++', 'haskell', 'prolog', 'minizinc', 'vba', 'html', 'css', 'javascript'])
print(s)
res = s.map(lambda x: print(x))
print(res)




