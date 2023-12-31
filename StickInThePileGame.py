"""
Stick Game

Tanat Piumsuwan 660631098
"""
import random
import numpy as np


playercanchoose = False
if playercanchoose:
    #Let the player choose the number of starting sticks?
    sticks = int(input("How many sticks (N) in the pile:"))         #ask for number of sticks in the pile
else:
    #Fix the number of starting sticks
    sticks = 20

maxpick = 2                                                         #Max number of sticks I can pick

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
    global playerpicked
    while True:
        pick = int(input(f"{name}, how many sticks you will take:"))  
        #input for number of sticks the user want
        if pick > maxpick:
        #invalid number of pick (take more than 2), warn the user
            print(f"No, you cannot take more than {maxpick} stick!")
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
            print(f"You take {pick} stick(s), there are {sticks} sticks in the pile.")
            break    

def botpick(sticks):
    #How many sticks the bot should pick, it should prioritize giving player the losing scenario
    #The losing scenario is when, in our turn, the number of stick mod maxpick+1 is 1
    if (sticks-1) % (maxpick+1) != 0:
    #just give the player the losing scenario
        pick = (sticks-1) % (maxpick+1)
    else:
    #losing scenario, all the bot can do is to random how many sticks it can pick and hope that the player is stupid
    #sticks = 1 the bot is definitely losing (check by min(maxpick,sticks))
        pick = random.randint(1,min(maxpick,sticks))
    return pick

def botplay(i):
    #Smart bot governed by modular
    global playerpicked
    playerpicked = False
    pick = botpick(sticks)
    picking(pick,i)
    print(f"I take {pick} stick(s), there are {sticks} sticks in the pile.")
    

while sticks > 0:
#until there are no stick left
    botplay(1) 
    if sticks < 1:
    #In case the bot pick the last stick and lose
        break
    playerplay(name,0)
    
    
    
print("Ok, there is no stick left in the pile. You spent {0} times, the player 2 spent {1} times.".format(counts[0],counts[1]))
if playerpicked:
    print("You took the last stick, I WON.")
else:
    print("I took the last stick, you win.")