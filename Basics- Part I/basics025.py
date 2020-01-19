print("Insert a number")
s = input()
print("Insert a list of letters")
lis = input().split(',')
if s in lis:
    print(True)
else:
    print(False)
