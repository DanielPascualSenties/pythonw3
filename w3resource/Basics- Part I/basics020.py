print("Insert a string")
s = input()
print("Insert the number of times it will be repeated")
n = int(input())
res = ""
for i in range(n):
    res = res + s
print(res)
