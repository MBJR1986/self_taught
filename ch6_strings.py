# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:37:45 2017

@author: MB047320
"""

#ch 6 challenges

"""1. print every character in the string "Camus".
"""
#for loop
string = "Camus"
for a in string:
    print(a)
    
#text answer by indexing (both work)
author = "Camus"
print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])

"""2. Write a program that collects two strings from a user, insert them into
    the string "Yesterday, I wrote a [response1]. I sent it to [response2]!
    and prints a new string.
"""

a = input("what did you write?")
b = input("who did you you send it to?")
statement = "Yesterday, I wrote a {}. I sent it to {}.".format(a,b)
print(statement)


"""3. use a method to make the string "aldous Huxley was born in 1894." grammatically
        correct by capitalizing the first letter in the sentence.
"""
x = "aldous".capitalize()
y = " Huxley was born in 1894."
words = x+y
print(words)



"""4. Take the string "Where now? Who now? When now?" and call a method that returns
        a list that looks like: ["Where now?", "Who now?", "When now?"].
"""

x = "Where now? Who now? When now?"
y = x.split("?")
print(y)



"""5. Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn it
        itno a grammatically correct string. There should be a space between each word, 
        but no space between period and last word.
"""

x = ["The", "fox", "jumped", "over", "the", "fence", "."]
y = " ".join(x)
y = y[0: -2] + "."
print(y)

"""6. Replace every instance of "s" in "A screaming comes across the sky" with a 
        a dollar sign.
"""

x = "A screaming comes across the sky"
y = x.replace('s', '$')
print(y)    

"""7.Use a method to find the first index of the character "m" in the string
    'Hemingway"
"""

search = "Hemingway"
search.index('m')


"""8. create the string " three three three" using concatenation, then again 
    using multiplication
"""

string1 = "three"
string_1 = string1 + string1 +string1
print(string_1)
mult = string1*3
print(mult)

"""Slice the string "It was a bright cold day in April, and the clocks were striking thirteen"
    to only include the characters before the comma.
"""
#slice by index...

#solutions: http://tinyurl.com/hapm4dx 