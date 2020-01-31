def without_duplicates(lis):
    new_list = []
    for i in lis:
        if i not in new_list:
            new_list += i

    return new_list


x = without_duplicates(['1', '2', '3', '4', '5', '5', '5', '5', '5', '6'])
print(x)
