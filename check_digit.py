#!/usr/bin/python3
number = [2, 8, 2]

i = 0
j = 0
total = 0
sum = 0
while i < len(number):   # learn how to implement this in a for loop 
     if i % 2 == 0:
        total += number[i]
     i += 1 
new_total = total * 3 

while j < len(number):
     if j % 2 != 0:
         sum  += number[j] 
     j += 1 

sum1 = new_total + sum 

last_digit = sum1 % 10
if last_digit == 0:
   result = 0
else:   
    result = 10 - last_digit

 
print(new_total)
print(sum1)
print(last_digit)
print(result)