dic = {'a': 12, 'b': 15, 'c': 3}


def find(x):
    k = dic.keys()
    print(k.__contains__(x))


find('ba')