def identify_sequence(seq):
    differences = [0,0]
    differences[0] = seq[1]-seq[0]
    differences[1] = seq[2] - seq[1]
    if (differences[0] == differences[1]):
        print("Arithmetic progression")
    else:
        print("Geometric progression")


identify_sequence([2,4,7])