def word_maker(string_so_far, letters_left):
    if not letters_left:
        print(string_so_far)
    else:
        for i in range(len(letters_left)):
            print(i)
            addition = letters_left[i]
            current = letters_left
            del current[i]
            print(letters_left)
            word_maker(string_so_far + addition, current)


word_maker("", ['a', 'e', 'i', 'o', 'u'])
# TODO fails miserably