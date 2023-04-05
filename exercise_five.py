# Oliver Sigwarth
# Exercise 5: Pig Latin
# Exercise from "Python Workout: 50 ten-minute exercises" by Reuven M. Lerner
# Created: 3/27/2023
# Modified: 3/27/2023
# ------------------------------------------------------------------------------
#                                   Objective
# Write a function (pig_latin) that takes a string as input, assumed English word,
# and returns the translation of the word into Pig Latin.
#
#   Pig Latin...
#       - If the word begins with a vowel (a, e, i , o u),
#         add "way" to the end of the word.
#       - If the word begins with any other letter, take the
#         first letter and move it to the end of the word and add "ay".
def pig_latin(phrase):
    way_letters = ["a", "e", "i", "o", "u"]
    updated_phrase = ""
    for char in way_letters:
        if char.lower() == phrase[0]:
            updated_phrase = phrase + "way"
            break
    updated_phrase = phrase[1:] + phrase[0] + "ay"
    return updated_phrase

# print(pig_latin("Hello"))