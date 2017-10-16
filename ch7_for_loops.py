# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 13:23:09 2017

@author: Mark Burghart
"""
# Ch. 7 Loops Notes and problems

###################
### For Loops   ###
###################

#example for loop
name = "Ted"
for character in name:
    print(character)
    
    
#for loop for iterating over items in list
shows = ["GOT"
         ,"Narcos"
         ,"Vice"]
for show in shows:
    print(show)
    
    
#use for loop to change items in mutable iterable (list ex)
i = 0 #index variable
for show in shows:
    new = shows[i]
    new = new.upper()
    shows[i] = new
    i += 1
print(shows)


#alternative pythonic method
shows = ["GOT"
         ,"Narcos"
         ,"Vice"]
for i, show in enumerate(shows): #enumerate function iterates over each row without counter index variable
    new = shows[i]
    new = new.upper()
    shows[i] = new
print(shows)


#iterating through a range
for i in range(1,11):
    print(i)


######################
### While Loops    ###
######################
x = 10
while x > 0:
     print('{}'.format(x))
     x -= 1
print("Happy New Year!")

#####################
### Nested Loops  ###
#####################
#nested for loop
for i in range(1, 3):
    print (i)
    for letter in ["a", "b", "c"]:
        print(letter)
        
#using two for loops to combine lists (with addition)
list1 = [1,2,3,4]
list2 = [5,6,7,8]
full = [] #empty list to contain combined list
for i in list1:
    for j in list2:
        full.append(i + j)


#######################
###     Challenges  ###
#######################
""" 
1. Print items in list.
"""
list_movie = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for i in list_movie:
    print(i)        
    

"""
2. Print all numbers from 25 to 50
"""

for i in range(25, 51):
    print(i)


"""
3. print each item in the list from the first challenge and their index
"""
for i in list_movie:
    print(i)
    print(list_movie.index(i))
    

"""
4. multiply all the numbers in a list with all the numbers in another, and append to new list
"""
list1 = [8,19,148,4]
list2 = [9,1,33,83]

new = []
for i in list1:
    for j in list2:
        mult = i*j
        new.append(mult)
print(new)
    






