def DNA_strand(dna):
    """This function iterates through the DNA strain
    given and changes the letters as prescribed.
    It is a challenge found in codewars. The link is in the read me found in this repo."""
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


strain = "ATTCG"  # when passed to the function this should print TAAGC
print(DNA_strand(strain))
