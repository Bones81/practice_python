# make a 2 player RPS game
# choices = ["R", "P", "S"]
# choice1 = input("1st Player, choose R, P, or S: ")
# while(choice1 not in choices):
#     choice1 = input("Please choose either R, P, or S: ")

# choice2 = input("2nd Player, choose R, P, or S: ")
# while(choice2 not in choices):
#     choice2 = input("Please choose either R, P, or S: ")

# if (choice1 == "R"):
#     if (choice2 == "P"):
#         print("Player 2 wins. Paper covers rock")
#     elif (choice2 == "S"):
#         print("Player 1 wins. Rock crushes scissors")
#     else:
#         print("Both chose Rock. Tie.")
# elif (choice1 == "P"):
#     if (choice2 == "P"):
#         print("Both chose Paper. Tie.")
#     elif (choice2 == "S"):
#         print("Player 2 wins. Scissors cuts paper.")
#     else: # p2 chose rock
#         print("Player 1 wins. Paper covers rock.")
# else:
#     if (choice2 == "P"):
#         print("Player 1 wins. Scissors cuts paper.")
#     elif (choice2 == "S"):
#         print("Both chose Scissors. Tie.")
#     else:
#         print("Player 2 wins. Rock crushes scissors.")

##### Another way of doing it
import random as rd
choices = ['r','p','s']
r_outcomes = {
    "r": "tie",
    "p": "loss",
    "s": "win"
}

p_outcomes = {
    "r": "win",
    "p": "tie",
    "s": "loss"
}

s_outcomes = {
    "r": "loss",
    "p": "win",
    "s": "tie"
}
logic = {
    "r": r_outcomes, 
    "p": p_outcomes, 
    "s": s_outcomes
}

choice1 = input("Player 1, choose rock, paper, or scissors (Enter 'r', 'p', or 's'): ").lower()
while(choice1 not in choices):
    choice1 = input("Invalid. Choose either 'r', 'p', or 's' only: ").lower()
random_num = rd.randint(0,2)
choice2 = choices[random_num]

print(choice1, choice2, logic[choice1][choice2])