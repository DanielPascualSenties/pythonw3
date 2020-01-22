print("Write a series of comma separated numbers")
inp = input()
lis = list(inp.split(","))
counter = 0
for i in range(len(lis)):
    if lis[i] == '4':
        counter += 1
print(str(counter))
