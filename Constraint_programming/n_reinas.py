from typing import List

from constraint import *


problem = Problem()
numpieces = 4
rows = [1,2,3,4]

problem.addVariables([1,2,3,4], range(numpieces))



def not_same_column(x, y):
    return x != y


def not_same_diagonal_downwards(row1, row2, colu1, colu2):
    return row1-colu1 != row2-colu2


def not_same_diagonal_upwards(row1, row2, colu1, colu2):
    print(str(row1) + " " + str(row2) + " " + str(colu1) + " " + str(colu2))
    if row1-colu1 != row2-colu2:
        print("Este si")
        return True
    else:
        print("Este no")
        return False


for f1 in rows:
    for f2 in rows:
        if f1 < f2:
            problem.addConstraint(AllDifferentConstraint())
            print(f1)
            print(f2)
            problem.addConstraint(not_same_diagonal_downwards, (rows[f1], rows[f2], f1, f2))
            #problem.addConstraint(lambda row1, row2: not_same_diagonal_upwards(row1, row2, col1, col2), (col1, col2))
            #problem.addConstraint(lambda row1, row2: row1 != row2,(col1, col2))
#            problem.addConstraint(lambda row1, row2: (row1 - col1) != (row2 - col2),
#                                  (col1, col2))
#            problem.addConstraint(lambda row1, row2: (row1 - row2) != (col2 - col1),
#                                  (col1, col2))
solutions = problem.getSolutions()
print(solutions)
