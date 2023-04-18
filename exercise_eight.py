# Oliver Sigwarth
# Exercise 8: Sorting a String
# Exercise from "Python Workout: 50 ten-minute exercises" by Reuven M. Lerner
# Created: 4/18/2023
# Modified: 4/18/2023
# ------------------------------------------------------------------------------
#                                   Objective
# Write a function (strsort) that takes a string and returns it sorted from
# lowest to highest Unicode value.
def strsort(phrase):
    phrase_list = [phrase[i] for i in range(len(phrase))]
    newPhrase = ""
    phrase_list = sorted(phrase_list)
    for char in phrase_list:
        newPhrase += char
    return newPhrase


print(strsort("acb"))
