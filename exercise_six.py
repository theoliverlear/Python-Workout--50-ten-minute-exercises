# Oliver Sigwarth
# Exercise 6: Pig Latin Sentence
# Exercise from "Python Workout: 50 ten-minute exercises" by Reuven M. Lerner
# Created: 3/28/2023
# Modified: 3/28/2023
# ------------------------------------------------------------------------------
#                                   Objective
# Write a function (pl_sentence) that takes a string containing several
# words separated by spaces and translate the words to Pig Latin.
#
#   Pig Latin...
#       - If the word begins with a vowel (a, e, i , o u),
#         add "way" to the end of the word.
#       - If the word begins with any other letter, take the
#         first letter and move it to the end of the word and add "ay".
from exercise_five import pig_latin
def pl_sentence(sentence):
    new_phrase = ""
    new_phrase_array = sentence.split(" ")
    for word in new_phrase_array:
        new_phrase += pig_latin(word) + " "
    return new_phrase

print(pl_sentence("David is the best husband ever. I love him so much."))