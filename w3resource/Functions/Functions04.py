def reverse_string(s):
    rev = ""
    for i in s:
        rev = i + rev
    return rev


x = reverse_string("galleta")
print(x)