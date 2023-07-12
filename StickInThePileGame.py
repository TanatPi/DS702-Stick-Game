# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 17:42:43 2023

@author: Tanat 660631098
"""

sticks = int(input("How many sticks (N) in the pile:"))             #ask for number of sticks in the pile
print("There are {} sticks in the pile.".format(sticks))
name = input("What is your name:")                                  #ask for user's name
i = 0
while sticks > 0:
#until there are no stick left
    pick = int(input("{}, how many sticks you will take (1 or 2):".format(name)))   
    #input for number of sticks the user want
    if pick > 2:
    #invalid number of pick (take more than 2), warn the user
        print("No, you cannot take more than 2 stick!")
    elif sticks - pick < 0:
    #invalid number of pick (take more than available sticks), warn the user
        print("There are not enough stick to take.")
    elif pick < 1:
    #invalid number of pick (take less than 2), warn the user
        print("No, you cannot take less than 1 stick!")
    else:
    #Valid pick, count attemp and get leftover sticks
        sticks -= pick
        i += 1
    print("There are {} sticks in the pile.".format(sticks))
print("Ok, there is no stick left in the pile. You spent {} times.".format(i))