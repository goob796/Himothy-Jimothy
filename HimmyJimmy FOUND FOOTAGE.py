#Team project. Antonio Lucky Ducky
import random
def main():
    #accepts no aguements
    #calls all functions to play the number of games specified
    another = 'y'
    while another == 'y':
        nums = first_roll()
        output_dice(nums)
        
        another = input('Play another game? (y/n)')
    
def output_dice(nums):
    #accepts dice
    #outputs each die in the list
    print('-----Roll #',total,'-----')
    for num in range(1,12+1):
        print('Die\t',num,':', nums[num-1])

def roll_die():
    #accepts no arguements
    #returns a random integer from 1 to 6
    Roll = random.randint(1,6)
    return Roll

def first_roll():
    #accepts no arguements
    #uses roll_die to generate a list of 6 integers
    #returns a list of 6 random integers
    nums = []
    total1 = 0
    while total1 < 12:
        num = roll_die()
        total1 += 1
        nums.append(num)
    return nums

def count_frequency(nums, die):
    #accepts a list of 6 random integers and a target die
    #returns how often that target die occurs in the list
    pass

def find_mode(nums):
    #accepts a list of dice.
    #uses count_frequency(dice, die) to determine how often each die occurs.
    #returns the mode
    pass

def list_unmatched_dice(nums):
    #accepts a list of dice.
    #determines which dice need rerolled
    #returns a list of indexes to reroll
    pass

def reroll_one(nums, index):
    #accepts a list of dice and an index.
    #uses roll_die to reroll that index
    #returns a new list with that index rerolled
    pass

def reroll_many(nums):
    #accepts a list of dice
    #calls list_unmatched_dice() and reroll_one() to reroll each die != the mode.
    #returns a list of rerolled dice.
    pass