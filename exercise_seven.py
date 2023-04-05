# Oliver Sigwarth
# Exercise 7: Ubbi Dubbbi
# Exercise from "Python Workout: 50 ten-minute exercises" by Reuven M. Lerner
# Created: 3/29/2023
# Modified: 4/4/2023
# ------------------------------------------------------------------------------
#                                   Objective
# Write a function (ubbi_dubbi) that takes a single word as an argument
# and returns a string translated to Ubbi Dubbi.
#
#   Ubbi Dubbi...
#       - Every vowel (a, e, i, o, u) is prefaced with "ub."
def ubbi_dubbi(word):
    word_len = len(word)
    new_word = ""
    for i in range(word_len):
        if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
            new_word += "ub" + word[i]
        else:
            new_word += word[i]
    return new_word
print(ubbi_dubbi("program"))
