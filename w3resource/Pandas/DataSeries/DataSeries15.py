import pandas

s = pandas.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 3])

print(s)

mean = s.mean()
print("Mean: " + str(mean))
sd = s.std()
print("Standard Deviation: " + str(sd))
