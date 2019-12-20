n1 = 36
n2 = 12

m = min(n1, n2)
rng = range(2, m+1)
res = 1
for i in rng:
    if n1 % i == 0 and n2 % i == 0:
        res = i

print(res)
