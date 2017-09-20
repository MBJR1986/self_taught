# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:13:41 2017

@author: Mark
"""

# print 3 strings

x = "sup"
y = "hello"
z = x + y
print(x)
print (y)
print (z)

print("this is another way of printing a string")


# 2. Write program that prints a message if a variable is less than 10, and 
#   different message if greater than or equal to 10.

for i in range(15):
    if i < 10:
        print(i)
        print("this value is less than 10")
    else:
        print(i)
        print("this value is greater than or equal to 10")
        

# 3. write a program that prints a message if a variable is less than or equal
#        to 10, another if the variable is greater than 10 but less than or 
#        equal to 25, and another if the variable is greater than 25.

for i in range(30):
    if i < 10:
        print(i)
        print("kinda small")
    elif (i <= 25):
        print(i)
        print("in the middle")
    else:
        print(i)
        print("big number...")
    
#doing the same with a function parse()
def parse(num):
    num = int(num)
    if num <= 10:
        print("kinda small")
    elif (num <= 25):
        print("in the middle")
    else:
        print("big number...")
        
parse(10)        
parse(23)
parse(290)

# 4. Create a program that divides two variables and prints the remainder.
x =5
y = 2

rem = x%y
print(rem)
        
# 5. Create a program that takes two variables, divides them, and prints the quotient
x = 10
y = 3
quo = x//y
print(quo)
        
# 6. Write a program with a variable 'age' assigned to integer that prints different
#       strings depending on what integer age is.

age = 15
if age <= 10:
    print("young gun")
elif age <= 20:
    print("still got time")
else:
    print("done son")

        
#solutions: https://tinyurl.com/zx7o2v9