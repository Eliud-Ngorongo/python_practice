# numbers = [10, 290, 90, 87, 76, 6543, 0,99865, 100]
#
# for index, number in enumerate(numbers):
#   if number % 2 == 0 and number is not 0:
#     print("number is at index: ",index, 'and the number is: ',number)

# new_dict = {
#             "Eliud": "online",
#             "Njenga": "online",
#             "Nelly": "online"
#         }
#
# number_of_people = 0
# for key in (new_dict):
#   if new_dict[key] == "online":
#     number_of_people += 1
# print(number_of_people)
#
# def only_ints(a, b):
# a func that checks if both a and b are ints
#   if type(a) == int and type(b) == int:
#       return True
#   return False
#
#
# print(only_ints(10, "True"))

# def double_letter(string):
# a func that checks if a string has 2 concurrent letters
#     for letter in range(len(string) - 1):
#         if string[letter] == string[letter + 1]:
#             return True
#     return False
#
# print(double_letter("Anes"))


def add_dots(string):
    # this func adds a fullstop after every letter in a given string
    new = '.'.join(string)
    return new


def remove_dots(string):
    # this func replaces fullstops with no space in a given string
    new = string.replace('.', '')
    return new


print(remove_dots(add_dots("test")))  # return test


def count(string):
    # this func counts the number of syllables in given string
    counter = 1
    for letter in string:
        if letter == "-":
            counter += 1
    return counter



print(count("ter-min-a-tor"))
