# Oliver Sigwarth
# Exercise 4: Hexadecimal Output
# Exercise from "Python Workout: 50 ten-minute exercises" by Reuven M. Lerner
# Created: 3/25/2023
# Modified: 3/26/2023
# ------------------------------------------------------------------------------
#                                   Objective
# Write a hex_output function that takes a hex number and returns the decimal equivalent.
#
# Hexadecimal | Decimal |
#      0      |    0    |
#      1      |    1    |
#      2      |    2    |
#      3      |    3    |
#      4      |    4    |
#      5      |    5    |
#      6      |    6    |
#      7      |    7    |
#      8      |    8    |
#      9      |    9    |
#      A      |   10    |
#      B      |   11    |
#      C      |   12    |
#      D      |   13    |
#      E      |   14    |
#      F      |   15    |
def hex_to_decimal(h_decimal):
    new_h_decimal = []
    for i in range(len(h_decimal)):
        new_h_decimal.append(h_decimal[i])
    if new_h_decimal[0] == "0" and new_h_decimal[1] == "x":
        for i in range(2):
            new_h_decimal.pop(0)
    sum = 0
    h_decimal_length = len(new_h_decimal) - 1
    for i in range(0, h_decimal_length + 1):
        match new_h_decimal[i]:
            case "A":
                sum += (16**h_decimal_length) * 10
                h_decimal_length -= 1
            case "B":
                sum += (16**h_decimal_length) * 11
                h_decimal_length -= 1
            case "C":
                sum += (16**h_decimal_length) * 12
                h_decimal_length -= 1
            case "D":
                sum += (16**h_decimal_length) * 13
                h_decimal_length -= 1
            case "E":
                sum += (16**h_decimal_length) * 14
                h_decimal_length -= 1
            case "F":
                sum += (16**h_decimal_length) * 15
                h_decimal_length -= 1
            case _:
                sum += (16**h_decimal_length) * int(new_h_decimal[i])
                h_decimal_length -= 1
    return sum

print(hex_to_decimal("0x50"))
print(hex_to_decimal("2A5"))