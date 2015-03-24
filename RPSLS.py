# Rock-paper-scissors-lizard-Spock template

import random
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name): #function to assign a number to name 
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Are you sure you want to throw THAT?"
        

def number_to_name(number):# function to assign a number to name
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Error in assigning number to name."


def rpsls(player_choice): 
    print "" # print a blank line to separate consecutive games
    print "Player chooses", player_choice # message for the player's choice
    player_number = name_to_number(player_choice) # convert the player's choice to player_number
    comp_number = random.randrange(0, 4) # compute random guess for comp_number
    comp_choice = number_to_name(comp_number) # convert comp_number to comp_choice
    print "Computer chooses", comp_choice # print out the message for computer's choice
    direction = (comp_number - player_number) % 5 # compute difference of comp_number and player_number modulo five
    if direction == 1 or direction == 2:
        print "Computer wins!" # if clockwise, computer wins
        print ""
    elif direction == 3 or direction == 4:
        print "Player wins!" # if counter clockwise, Player wins
        print ""
    elif direction == 0:
        print "Player and computer tie!" # if no movement, tie
        print ""
    else:
        print "Error determining winner."


#rpsls("rock")
#rpsls("Spock")
#rpsls("paper")
#rpsls("lizard")
#rpsls("scissors")

print ""
player_choice = raw_input("What would you like to throw? ")
rpsls(player_choice)
