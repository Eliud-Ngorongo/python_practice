def only_even(string):
    # prints the letters at the even placed index
    number = 0
    for letter in list(string):
        if number % 2 == 0:
            print(letter)
        number += 1
# only_even("pynative") this will print p, n, t, v