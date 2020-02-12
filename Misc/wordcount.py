palabras = []
faltando = []
with open('texto.txt', 'r') as f:
    first_line = f.readline()
    second_line = f.readline()
    for word in second_line.split():
        palabras.append(word)
    for word in first_line.split():
        if word not in palabras:
            faltando.append(word)


print(faltando)
