palabras = []
faltando = []
with open('texto.txt', 'r') as f:
    second_line = f.readline()
    first_line = f.readline()
    for word in first_line.split():
        palabras.append(word)
    for word in second_line.split():
        if word not in palabras:
            faltando.append(word)

print(palabras)
print(faltando)

