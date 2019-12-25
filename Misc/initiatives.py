from operator import itemgetter
import random
initiatives = [["Aurora", 9], ["Perno", 7], ["Ochesto", 0], ["Yara",3]]

for i in initiatives:
    r1 = random.randint(1, 10)
    r2 = random.randint(1, 10)
    i[1] += r1 + r2


s = sorted(initiatives, key=lambda x: x[1], reverse=True)
print(s)