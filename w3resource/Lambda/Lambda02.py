def funcion_multiplicadora(n):
    return lambda a: a * n


x = funcion_multiplicadora(3)(5)


print(str(x))