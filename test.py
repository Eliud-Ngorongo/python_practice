
def xo(s):
    new = []
    new1 = []
    for elm in s:
        if elm == 'x':
            new.append(elm)
        elif elm == 'o':
            new1.append(elm)
        elif elm != 'x' and elm != 'o':
            return True
    if len(new) == len(new1):
        return True
    else:
        return False


print(not xo('xxxoo'), 'False expected')

