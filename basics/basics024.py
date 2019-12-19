print("Insert a letter")
s = input()
char = s[0]
if char in ('a', 'e', 'i', 'o', 'u'):
    print("¡Vocal!")
else:
    print("Consonante")
