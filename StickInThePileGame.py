"""
Stick Game

Tanat Piumsuwan 660631098
"""
import random
import numpy as np


sticks = int(input("How many sticks (N) in the pile:"))             #ask for number of sticks in the pile
print("There are {} sticks in the pile.".format(sticks))            
name = input("What is your name:")                                  #ask for user's name
counts = np.zeros(2, dtype=int)                                     #2 players for now

def playerplay(name,i):
    #What to do when a participant about to pick sticks
    global sticks,counts
    while True:
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
            counts[i] += 1
            break
    print(f"There are {sticks} sticks in the pile.")
    
def botplay(name,i):
    #I choose smart player 2 (may improve in the future or add stochastic property to its decision making)
    global sticks,playerpicked,counts
    if sticks == 0:
    #Make sure that if there are 0 sticks, the player 2 doesn't pick and win 
        playerpicked = True
        print("The {} did not picked any from the pile.".format(name))
    else:
        playerpicked = False
        counts[i] += 1
        if sticks > 4:
            pick = 2
            sticks -= pick
        elif sticks == 4:
        #This leads to player's winning scenario, may change
        #If there are 3 left, player then  pick 2. If there are 2 left, player then pick 1.
            pick = random.choice([1,2])         #For now I add random choice to make the game not repetitive.
            sticks -= pick
        elif sticks == 3:
            pick = 2
            sticks -= pick
        elif sticks < 3:
            pick = 1
            sticks -= pick
        print(f"The player 2 picked {pick} from the pile.")
    

while sticks > 0:
#until there are no stick left
    playerplay(name,0)
    botplay("player 2",1)
    

        
    print("There are {} sticks in the pile.".format(sticks))  
print("Ok, there is no stick left in the pile. You spent {0} times, the player 2 spent {1} times.".format(counts[0],counts[1]))
if playerpicked:
    print("You took the last stick, you lose.")
else:
    print("Player 2 took the last stick, you win.")