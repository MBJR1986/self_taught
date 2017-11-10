# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:00:12 2017

@author: Mark Burghart
"""

# ch10 tying it all together...

"""
1. Build hangman game
"""

#todo: not printing board, also doesn't print duplicate letters (ie title, t has to be selected twice)

def hangman(word):  #stores game in hangman function; word represent the word player 2 needs to guess
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
        ]
    rletters = list(word)
    board = ["_"]* len(word)
    win = False
    print("Welcome to Hangman")  
#loop that keeps the game going
    while wrong < len(stages) - 1: #game/loop continues until wrong < length of stages - 1
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters \
                    .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
              .join(stages[0: e])) #prints the hangman board 'stages'
        if "_" not in board:
            print("You Win!!!")
            print(" ".join(board))
            win = True
            break
    if not win: 
        print("\n"
              .join(stages[0: \
                wrong]))
        print("You LOSE!!! It was {}."
              .format(word))