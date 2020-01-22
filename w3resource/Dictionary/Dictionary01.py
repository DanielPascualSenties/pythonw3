import operator
dic = {'a': 12, 'b': 15, 'c': 3}

ascending = sorted(dic.items(), key=operator.itemgetter(1))
print(ascending)

descending = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
print(descending)

