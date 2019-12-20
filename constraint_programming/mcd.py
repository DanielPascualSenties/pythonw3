from constraint import *

problem = Problem()
n1 = 51
n2 = 36

mini = min(n1,n2)
top = range(mini)
problem.addVariable(top,top)

for num in top:
    if num > 0:
        problem.addConstraint(lambda numer: n1 % numer == 0, (num))
#    problem.addConstraint(n2 % num == 0)

solutions = problem.getSolutions()
print(solutions)
