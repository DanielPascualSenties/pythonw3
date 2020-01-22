print("Write the number of feet you want added")
n = float(input())

whole_part = int(n)
partial_part = n - float(whole_part)

if whole_part >= 5280:
    miles = int(whole_part/5280)
    print(str(miles) + " miles")
womiles = whole_part % 5280
if womiles >= 3:
    yards = int(womiles / 3)
    print(str(yards) + " yards")
woyards = womiles % 3
print(str(woyards) + " feet")
whole_inches = int(12 * partial_part)
print(str(whole_inches) + " inches")
