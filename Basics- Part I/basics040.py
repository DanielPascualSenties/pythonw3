import math


def pythagoras(x_1, x_2, y_1, y_2):
    dif_x = x_1 - x_2
    dif_y = y_1 - y_2
    sq = dif_x*dif_x + dif_y*dif_y
    return math.sqrt(sq)


print("X coordinate of point 1")
x1 = int(input())
print("Y coordinate of point 1")
y1 = int(input())
print("X coordinate of point 2")
x2 = int(input())
print("Y coordinate of point 2")
y2 = int(input())

print(str(pythagoras(x1, y1, x2, y2)))
