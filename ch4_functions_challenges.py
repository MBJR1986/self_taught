# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:03:21 2017

@author: Mark Burghart
"""

# Self Taught ch4 Functions problems

"""1. write function that takes a numbers as an input and returns that 
   number squared."""
   
def f(x):
    return x**2
    

"""2. Create a function that accepts a string as a parameter and prints it"""

def stringz(some_string):
    print(some_string)


"""3. Write a function that takes three required parameters and two optional parameters"""

def temp(x, y = 10, z = 2):
    final = x + y + z
    print(final)

"""4. write a program with two functions: 1 should take an integer as a parameter
and return the result of the integer divided by 2. 2 should take an integer as a parameter
and return the result of the integer multiplied by 4.  Call first function, save result
as a variable, and passit as a parameter to 2nd function.
"""

def func_one(integer):
    return integer/2
    
def func_two(integer):
   return integer * 4
    
x = func_one(10)
func_two(x)
    

"""5. write a function that converts a string to a float and returns the result.
use exception handling to catch the exception that could occur."""

def string_to_float(string):
    try:
        string = float(string)
        print(string)
    except ValueError:
        print("Invalid Type")

string_to_float("winner")
string_to_float("10")

"""6. add a docstring to all of the functions you wrote in challenges 1-5."""
#That's going to be a no for me dawg.