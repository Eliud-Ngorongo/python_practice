def DNA_strand(dna):
    new_string = ''
    for letter in dna:
        if letter == "A":
            new_string += 'T'
        if letter == 'T':
            new_string += 'A'
        if letter == 'G':
            new_string += 'C'
        if letter == 'C':
            new_string += 'G'
    return new_string

