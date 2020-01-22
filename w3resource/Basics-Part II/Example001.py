lis = [1, 2, 3, 4, 2, 6, 7, 8, 9]

without_duplicates = []
ok = True
for i in range(0,len(lis)):
    if lis[i] in without_duplicates:
        ok = False
        break
    else:
        without_duplicates.append(lis[i])

if ok:
    print("There are no duplicates")
else:
    print("Things are not ok")