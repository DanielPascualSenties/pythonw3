bills = [500, 200, 100, 50, 20, 10, 5, 2, 1]


def find_adequate_bill(num):
    for i in range(9):
        if num > bills[i]:
            return i
    return 8


def pay_with_bills_greedy(num):
    change = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    while num > 0:
        bill = int(find_adequate_bill(num))
        change[bill] += 1
        num -= bills[bill]
    return change


print(pay_with_bills_greedy(523))
