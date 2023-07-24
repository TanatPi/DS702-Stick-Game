"""
Stick Game

Tanat Piumsuwan 660631098
"""
import random
import numpy as np


playercanchoose = False
if playercanchoose:
    #Let the player choose the number of starting sticks?
    sticks = int(input("How many sticks (N) in the pile:"))             #ask for number of sticks in the pile
else:
    #Fix the number of starting sticks
    sticks = 20

name = input("What is your name:")                                  #ask for user's name
print(f"There are {sticks} sticks in the pile.")            
counts = np.zeros(2, dtype=int)                                     #2 players for now


def picking(pick,i):
    #What happens when sticks are picked
    global sticks,counts
    sticks -= pick
    counts[i] += 1
    
def playerplay(name,i):
    #What to do when a participant about to pick sticks
    global sticks,counts,playerpicked
    while True:
        print(f"There are {sticks} sticks in the pile.")  
        pick = int(input(f"{name}, how many sticks you will take (1 or 2):"))  
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
            picking(pick,i)
            playerpicked = True
            print(f"I take {pick} stick(s), there are {sticks} sticks in the pile.")
            break    

def botplay(name,i):
    #I choose smart player 2 (may improve in the future or add stochastic property to its decision making)
    global sticks,counts,playerpicked
    if sticks == 0:
    #Make sure that if there are 0 sticks, the player 2 doesn't pick and win 
        playerpicked = False
        print(f"The {name} did not picked any from the pile.")
    else:
        pick = 2
        picking(pick,i)
        print(f"The {name} picked {pick} from the pile.")
    

while sticks > 0:
#until there are no stick left
    playerplay(name,0)
    botplay("player 2",1) 
    
    
print("Ok, there is no stick left in the pile. You spent {0} times, the player 2 spent {1} times.".format(counts[0],counts[1]))
if playerpicked:
    print("You took the last stick, I WON.")
else:
    print("I took the last stick, you win.")