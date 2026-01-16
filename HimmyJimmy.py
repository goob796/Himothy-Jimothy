#Team project. Antonio Lucky Ducky
import random

def main():
    #accepts no aguements
    #calls all functions to play the number of games specified
    pass

def output_dice(dice):
    #accepts dice
    #outputs each die in the list
    pass

def roll_die():
    #accepts no arguements
    #returns a random integer from 1 to 6
    pass

def first_roll():
    #accepts no arguements
    #uses roll_die to generate a list of 12 integers
    #returns a list of 12 random integers
    pass

def count_frequency(dice, number):
    #accepts a list of 12 random inegers and a target die
    #returns how often that target die occurs in the list
    pass

def find_mode(dice):
    #accepts a list of dice.
    #uses count_frequency(dice, die) to determine how often each die occurs.
    #returns the mode
    pass

def list_unmatched_dice(dice):
    #accepts a list of dice.
    #determines which dice need rerolled
    #returns a list of indexes to reroll
    pass

def reroll_one(dice, index):
    #accepts a list of dice and an index.
    #uses roll_die to reroll that index
    #returns a new list with that index rerolled
    pass

def reroll_many(dice):
    #accepts a list of dice
    #calls list_unmatched_dice() and reroll_one() to reroll each die != the mode.
    #returns a list of rerolled dice.
    pass