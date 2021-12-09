def check_number(my_list):
   """This functions checks if the first number
     is the same as the last number in a given list"""
   last = len(my_list) - 1
   for element in my_list:
      if my_list[0] == my_list[last]:
          return True
   return False

# some examples
numbers = [10, 20, 90, 10] 
print(check_number(numbers)) # returns True
numbers = [10, 20, 90, 10, 34, 10, 90]
print(check_number(numbers)) # returns False
