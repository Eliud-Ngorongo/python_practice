#!/usr/bin/python3
def reverse():
    new = []
    for i in range(97, 123):
        new.append(chr(i))
    #print(new)    
    print(new[::-1])


reverse()