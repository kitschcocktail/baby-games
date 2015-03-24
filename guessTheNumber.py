#!/usr/bin/env python
# "Guess the number" mini-project


#import Tkinter as tk
from Tkinter import *
import random
import math

num_range = 100
secret_number = random.randrange(0,100)
guesses_left = 7


# helper function to start and restart the game
def new_game():
    global secret_number
    global guesses_left
    if num_range == 100:
        guesses_left = 7
        secret_number = random.randrange(0,num_range)
    elif num_range == 1000:
        guesses_left = 10
        secret_number = random.randrange(0,num_range)
    else:
        print "Eroooooor in number range."
    print "New game. Range is from 0 to", num_range
    print "You have", guesses_left, "guesses to win."
    print ""
    

# define event handlers for control panel
def range100():
    """button that changes the range to [0,100) and starts a new game"""
    global num_range
    num_range = 100  
    new_game()

def range1000():
    """ button that changes the range to [0,1000) and starts a new game"""   
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    guess = E1.get() # get guess from input
    player_guess = int(guess) # change string input into integer
    global guesses_left
    print "You guessed", player_guess
    guesses_left -= 1 # decrement number of guesses at each turn
    if guesses_left == 1:
        print "You have", guesses_left, "guess left." # because grammar
    else:
        print "You have", guesses_left, "guesses left."
        
    if player_guess == secret_number:
        print "Correct!"
        print ""
        new_game() # game has ended, new game.
    elif guesses_left == 0:
        print "No more guesses. The number was", secret_number
        print ""
        new_game() # game has ended, new game.
    elif player_guess > secret_number:
        print "Lower!"
    elif player_guess < secret_number:
        print "Higher!"
    else:
        print "Error."
    print ""



master = Tk()
f = Frame(master, height=32, width=32)
f.pack()

b1 = Button(f, text='Range: 0 - 100', command=range100)
b1.pack()

b2 = Button(f, text='Range: 0 - 1000', command=range1000)
b2.pack()


l2 = Label(f, text="Guess the number: ")
l2.pack()


E1 = Entry(f)
E1.bind("<Return>", input_guess) # run input through input_guess
E1.pack()



master.title('Guess the Number')
master.mainloop()

