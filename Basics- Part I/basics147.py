print("First number:")
first_number = int(input())
print("Second number:")
second_number = int(input())

if first_number % second_number:
    print("Number " + str(first_number) + " is not divisible by " + str(second_number))
else:
    print("Number " + str(first_number) + " is divisible by " + str(second_number))
