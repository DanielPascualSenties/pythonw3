print("Insert a string")
s = input()
print("Insert the number of times it will be repeated")
n = int(input())
if len(s) < 2:
    head = s
else:
    head = s[0:2]
acc = ""
for i in range(n):
    acc += head
print(acc)
