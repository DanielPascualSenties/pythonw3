import constraint


board = \
    [[2, 9, 0, 7, 0, 0, 8, 6, 0],
     [0, 3, 1, 0, 0, 5, 0, 2, 0],
     [8, 0, 6, 0, 0, 0, 3, 0, 0],
     [0, 0, 7, 0, 5, 0, 0, 0, 6],
     [0, 0, 0, 3, 0, 7, 0, 0, 0],
     [5, 0, 0, 0, 1, 0, 7, 3, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 9],
     [0, 2, 0, 6, 0, 0, 0, 5, 0],
     [0, 5, 4, 0, 0, 8, 0, 7, 2]]


problem = constraint.Problem()

# Creamos variables del 11 al 99
for i in range(1, 10):
    problem.addVariables(range(i * 10 + 1, i * 10 + 10), range(1, 10))

# En cada fila, añadimos la restricción de que todos los elementos de la fila sean diferentes
for i in range(1, 10):
    problem.addConstraint(constraint.AllDifferentConstraint(), range(i * 10 + 1, i * 10 + 10))

# Lo mismo para las columnas
for i in range(1, 10):
    problem.addConstraint(constraint.AllDifferentConstraint(), range(10 + i, 100 + i, 10))

# Ahora delimitamos los nueve cuadrados de 3x3, y nos aseguramos que todos los números
# cada cuadrado sean diferentes
for i in [1, 4, 7]:
    for j in [1, 4, 7]:
        square = [10 * i + j, 10 * i + j + 1, 10 * i + j + 2, 10 * (i + 1) + j, 10 * (i + 1) + j + 1,
                  10 * (i + 1) + j + 2, 10 * (i + 2) + j, 10 * (i + 2) + j + 1, 10 * (i + 2) + j + 2]
        problem.addConstraint(constraint.AllDifferentConstraint(), square)

# Nos aseguramos de que las casillas que estaban ocupadas en el puzle original se respeten
for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            def c(variable_value, value_in_table=board[i][j]):
                if variable_value == value_in_table:
                    return True


            problem.addConstraint(c, [((i + 1) * 10 + (j + 1))])

solutions = problem.getSolutions()

# Recorremos la lista de soluciones y las imprimimos
for s in solutions:
    print(" =======================")
    for i in range(1, 10):
        print("|", end='')
        for j in range(1, 10):
            if j % 3 == 0:
                print(str(s[i * 10 + j]) + " | ", end='')
            else:
                print(str(s[i * 10 + j]), end=' ')
        print("")
        if i % 3 == 0 and i != 9:
            print(" -----------------------")
    print(" =======================")

if len(solutions) == 0:
    print("No solutions found.")
