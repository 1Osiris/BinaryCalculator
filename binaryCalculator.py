# Most of the logic and calculations are adapted from the general 
# formula for Binary --> Decimal

import math
def binaryCalcInt(binary: int, count: int = 0):
    try:
        count = 0 # acts the exponent that 2 is raised to
        sum = 0 # will be used as the central sum of all the calculations
        while binary != 0:
            bit = binary % 10
            if bit > 1: # cheching to see if the input is not in binary 
                raise Exception() # if current digit is not 1 or 0, an error is thrown
            sum += bit * (2**count) 
            count += 1 # updating the exponent 
            binary = binary // 10
        return sum
    except: 
        return "the input was not an integer or was not only 1s and 0s" # catches other errors like TypeErrors

print(binaryCalcInt(0)) # 0 -BinaryToDecimal-> 0
print(binaryCalcInt(1)) # 1 -BinaryToDecimal-> 1
print(binaryCalcInt(10)) # 10 -BinaryToDecimal-> 3
print(binaryCalcInt(1010)) # 1010 -BinaryToDecimal-> 100
print(binaryCalcInt(1100100)) # 1100100 -BinaryToDecimal-> 1000
print(binaryCalcInt(11100010)) # 11100010n -BinaryToDecimal-> 226
print(binaryCalcInt(13)) # 13 -BinaryToDecimal-> Invalid input, Error Thrown, because 13 is not a valid binary number
print(binaryCalcInt("1010")) # "1010" -BinaryToDecimal-> Invalid input, Error Thrown, because String is not a valid input type
