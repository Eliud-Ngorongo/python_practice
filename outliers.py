#!/usr/bin/python3
def find_outlier(integers):
    even, odd = [], []
    for number in integers:
        if number % 2 == 0:
            even.append(number)
        elif number % 2 != 0:
            odd.append(number)
    # print(len(odd))
    # print(len(even))
    if len(even) < len(odd):
        return even[0:]
    elif len(even) == len(odd):
        return integers # you can add the two lists, sort them then return the sorted list
    else:
        return odd[0:]


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(find_outlier(nums))