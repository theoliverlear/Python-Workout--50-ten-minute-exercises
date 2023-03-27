# Oliver Sigwarth
# Exercise 2: Summing numbers
# Exercise from "Python Workout: 50 ten-minute exercises" by Reuven M. Lerner
# Created: 3/18/2023
# Modified: 3/18/2023
# ------------------------------------------------------------------------------
#                                   Objective
# Write a mysum function that takes a variable number of arguments to sum the total value.
def mysum(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(mysum(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)) 