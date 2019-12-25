n1 = 36
n2 = 14

m = max(n1, n2)
lcm = n1 * n2
rng = range(m, n1*n2+1)
for i in rng:
    if i % n1 == 0 and i % n2 == 0:
        print("The lcm is " + str(i))
        break

