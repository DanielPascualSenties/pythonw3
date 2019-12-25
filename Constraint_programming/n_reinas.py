from constraint import *
from constraint import AllDifferentConstraint

problem = Problem()
numpieces = 3
cols = range(numpieces)
rows = range(numpieces)
problem.addVariables(cols, rows)


def not_same_column(x, y):
    return x != y


def not_same_diagonal_downwards(row1, row2, colu1, colu2):
    return row1-colu1 != row2-colu2


for col1 in cols:
    for col2 in cols:
        if col1 < col2:
            problem.addConstraint(AllDifferentConstraint())
            #problem.addConstraint(not_same_column, (col1, col2))
            problem.addConstraint(lambda row1, row2: not_same_diagonal_downwards(row1, row2, col1, col2), (col1, col2))
            #            problem.addConstraint(lambda row1, row2: row1 != row2,
            #                                  (col1, col2))
#            problem.addConstraint(lambda row1, row2: (row1 - col1) != (row2 - col2),
#                                  (col1, col2))
#            problem.addConstraint(lambda row1, row2: (row1 - row2) != (col2 - col1),
#                                  (col1, col2))
solutions = problem.getSolutions()
print(solutions)
