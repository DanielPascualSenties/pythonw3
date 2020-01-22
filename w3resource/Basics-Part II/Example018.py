def find_median(values_list):
    number_of_values = len(values_list)
    in_order = sorted(values_list)
    if number_of_values % 2:
        print("Caso impar")
        median_pos = int(number_of_values/2)
        print(str(in_order[median_pos]))
    else:
        print("Caso par")
        median_pos = int(number_of_values/2)
        print(str((in_order[median_pos-1]+in_order[median_pos])/2))


lis = [1, 4, 7, 34, 6354, 242, 535, 3, 12, 11]

find_median(lis)