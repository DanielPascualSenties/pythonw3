print("First number:")
first = int(input())
print("Second number:")
second = int(input())
print("Third number:")
third = int(input())

if first > second:
    small_1 = second
    if first > third:
        big = first
        small_2 = third
    else:
        big = third
        small_2 = first
else:
    small_1 = first
    if second > third:
        big = second
        small_2 = third
    else:
        big = third
        small_2 = second

print(small_1*small_1 + small_2*small_2 == big*big)