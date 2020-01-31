import math

from constraint import *


def print_sudoku(dic):
    le = len(dic)
    side = math.sqrt(le)
    for i in range(0, int(side)):
        print(str(dic[i*3]) + " " + str(dic[i*3+1]) + " " + str(dic[1*3+2]))
    print()


def different_row(ar):
    if ar[0] != ar[1] and ar[0] != ar[2] and ar[2] != ar[1]:
        return True


problem = Problem()
numrows = 3
cols = range(numrows*numrows)
vals = range(1, numrows+1)
problem.addVariables(cols, vals)
problem.addConstraint(different_row, cols)
solutions = problem.getSolutions()
print_sudoku(solutions[0])







