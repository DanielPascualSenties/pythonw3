def case_counter(s):
    lower = 0
    upper = 0
    for i in s:
        if i.islower():
            lower += 1
        if i.isupper():
            upper += 1
    print("Lower case letters: " + str(lower))
    print("Upper case letters: " + str(upper))


case_counter("One Banana Two Banana Three Banana Four Banana")