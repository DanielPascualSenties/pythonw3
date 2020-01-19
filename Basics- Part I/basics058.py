print("Write the number of integers you want added")
n = int(input())
total = 0
for i in range(1, n+1):
    total += i

print("The addition of the first " + str(n) + " integers is " + str(total))
