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


