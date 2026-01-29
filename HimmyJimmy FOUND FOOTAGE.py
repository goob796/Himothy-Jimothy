#Team project. Antonio Lucky Ducky.
import random

def main():
    #accepts no arguements
    #calls all functions to play the number of games specified
    # plays a single game

    print('Starting Game')

    nums = first_roll()
    rolls = 1
    output_dice(nums, rolls)

    # keep rolling until all dice are the same
    while True:
        same = True
        first = nums[0]
        for num in nums:
            if num != first:
                same = False

        if same:
            break

        nums = reroll_many(nums)
        rolls += 1
        output_dice(nums, rolls)

    print('Game completed in', rolls, 'rolls')

def output_dice(nums, roll_number):
    #accepts dice
    #outputs each die in the list
    
    print('\nRoll #', roll_number)
    print('---------------------')
    for i in range(len(nums)):
        print('Die', i + 1, ':', nums[i])


def roll_die():
    # accepts no arguments
    # returns a random integer from 1 to 6
    return random.randint(1, 6)


def first_roll():
    # accepts no arguments
    # uses roll_die to generate a list of 12 integers
    #returns a list of 12 random integers
    nums = []
    total = 0
    while total < 12:
        nums.append(roll_die())
        total += 1
    return nums


def count_frequency(nums, die):
    # accepts a list of dice and a target die
    # returns how often the target die occurs
    count = 0
    for num in nums:
        if num == die:
            count += 1
    return count


def find_mode(nums):
    # accepts a list of dice
    #uses count_frequency(dice, die) to determine how often each die occurs
    # returns the most common die value
    highest = 0
    mode = nums[0]

    for die in range(1, 7):
        freq = count_frequency(nums, die)
        if freq > highest:
            highest = freq
            mode = die
    return mode


def list_unmatched_dice(nums):
    #accepts a list of dice
    #determines whoch dice need rerolled
    #Retunrs a new list of indexes to reroll
    
    mode = find_mode(nums)
    indexes = []

    for i in range(len(nums)):
        if nums[i] != mode:
            indexes.append(i)
    return indexes


def reroll_one(nums, index):
    #accepts a list of dice and an index
    #uses roll_die to reroll that index
    #returns a new list with that index rerolled
    
    nums[index] = roll_die()
    return nums


def reroll_many(nums):
    #accepts a list of dice
    #calls list_unmathced_dice() and reroll_one() to reroll each die != the mode
    #returns a list of reolled dice
    
    indexes = list_unmatched_dice(nums)
    for index in indexes:
        nums = reroll_one(nums, index)
    return nums