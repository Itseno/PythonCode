from random import *
import sys

print("Welcome to Extreme RPS!")

t = ["Rock", "Paper", "Scissors"]

compChoice = t[randint(0,2)]

userChoice = False

comp_score = 0
player_score = 0

top_score = int(input("What's top score?"))

while userChoice == False:
    userChoice = input("Rock, Paper, Scissors?")
    if userChoice == compChoice:
        print("Sorry mate that's a tie!")
        print("Computer Score: " + str(comp_score))
        print("Player Score: " + str(player_score))
    elif userChoice == "Rock":
        if compChoice == "Paper":
            print("You lose!")
            comp_score = comp_score + 1
            print("Computer Score: " + str(comp_score))
            print("Player Score: " + str(player_score))
        else:
            print("You win!")
            player_score =+ top_score
            print("Computer Score: " + str(comp_score))
            print("Player Score: " + str(player_score))
    elif userChoice == "Paper":
        if compChoice == "Scissors":
            print("You lose!")
            comp_score =+ top_score
            print("Computer Score: " + str(comp_score))
            print("Player Score: " + str(player_score))
        else:
            print("You win!")
            player_score =+ top_score
            print("Computer Score: " + str(comp_score))
            print("Player Score: " + str(player_score))
    elif userChoice == "Scissors":
        if compChoice == "Rock":
            print("You lose!")
            comp_score =+ top_score
            print("Computer Score: " + str(comp_score))
            print("Player Score: " + str(player_score))
        else:
            print("You win!")
            player_score =+ top_score
            print("Computer Score: " + str(comp_score))
            print("Player Score: " + str(player_score))
    else:
        print("That's not a valid play. Check your spelling!")
    userChoice = False
    compChoice = t[randint(0,2)]
