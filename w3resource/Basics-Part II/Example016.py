import math

print("Insert the length of a side")
side1 = int(input())
print("Insert the number of another side")
side2 = int(input())
print("Is it the hypotenuse you are missing? y/n")
hyp = input()

if hyp == "y":
    print("Calculating hypotenuse")
    hypotenuse = math.sqrt(side1*side1 + side2*side2)
    print(str(hypotenuse))
else:
    print("Calculating leg")
    if side1 > side2:
        hypotenuse = side1
        known_leg = side2
    else:
        hypotenuse = side2
        known_leg = side1
    leg = math.sqrt(hypotenuse*hypotenuse - known_leg*known_leg)
    print(str(leg))
