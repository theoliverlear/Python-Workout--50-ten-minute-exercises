# Oliver Sigwarth
# Exercise 1: Number Guessing Game
# Exercise from "Python Workout: 50 ten-minute exercises" by Reuven M. Lerner
# Created: 3/17/2023
# Modified: 3/17/2023
# ------------------------------------------------------------------------------
#                                   Objective
# Write a function (guessing_game) that takes no arguments.
# When run, the function chooses a random integer between 0 and 100 (inclusive).
# Then ask the user to guess what number has been chosen.
# Each time the user enters a guess, the program indicates one of the following:
# - Too High
# - Too Low
# - Just Right
# If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
import random
def guessing_game():
    correct_guess = False
    random_int = random.randint(0, 100)
    while not correct_guess:
        guess = input("Guess what number has been chosen: ")
        guess = int(guess)
        if guess == random_int:
            print("Just Right")
            correct_guess = True
        elif guess < random_int:
            print("Too Low")
        elif guess > random_int:
            print("Too High")
guessing_game()
