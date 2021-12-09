def check_number(my_list):
    # returns true if the first number is the same as the last number in the list else return false

    last_number = len(my_list) - 1

    if my_list[0] == my_list[last_number]:
        return True
    else:
        return False

# new = [10, 20, 30, 40, 10]
# print(check_number(new)) this will print True
