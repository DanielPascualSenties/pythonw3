from typing import List


def filter_even(lis: List):
    new_list = []
    for i in lis:
        if not i % 2:
            new_list.append(i)
    return new_list


x = filter_even([1, 2, 3, 4, 5, 36, 8, 7])
print(x)
