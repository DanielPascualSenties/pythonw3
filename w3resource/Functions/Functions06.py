def in_range(minim, maxim, num):
    if minim > maxim:
        aux = minim
        minim = maxim
        maxim = aux
    return num in range(minim, maxim)


x = in_range(10, 14, 11)
print(x)
