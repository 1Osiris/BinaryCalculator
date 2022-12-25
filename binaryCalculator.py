# The function claculates the Decimal by iterating through the string using recursion 
# all of the logic for calculating specific values mostly follows from the general Binary -> Decimal formula 
def binaryCalcStr(binary: str):
    try:
        binaryNum = int(binary)
        if binaryNum == 0:
            return 0 # base case
        if binaryNum == 1:
            return 1 #base case
        bitplace = len(binary) - 1
        scalar = 2 ** bitplace
        bit = int(binary[0])
        if bit == 0:
            return binaryCalcStr(binary[1:])
        elif bit == 1:
            return scalar + binaryCalcStr(binary[1:])
    except: 
        return "the input was not a string or was not only 1s and 0s" #catches all errors

print(binaryCalcStr("0")) # "0" -BinaryToDecimial-> 0
print(binaryCalcStr("1")) # "1" -BinaryToDecimial-> 1
print(binaryCalcStr("10")) # "10" -BinaryToDecimial-> 2
print(binaryCalcStr("1010")) # "1010" -BinaryToDecimial-> 10
print(binaryCalcStr("1100100")) # "1100100" -BinaryToDecimial-> 100
print(binaryCalcStr("1100101010110")) # "1100101010110" -BinaryToDecimial-> 1686
print(binaryCalcStr(1010)) # 1010 -BinaryToDecimal-> Invalid input, Error Thrown, because Integer is not a valid type input
print(binaryCalcStr("abcd")) # "abcd"  -BinaryToDecimal-> Invalid input, Error Thrown, because "abcd" is not a valid binary number