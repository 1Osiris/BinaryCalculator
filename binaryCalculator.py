def binaryCalc(binary: str):
    try:
        binaryNum = int(binary)
        if binaryNum == 0:
            return 0
        if binaryNum == 1:
            return 1
        bitplace = len(binary) - 1
        scalar = 2 ** bitplace
        bit = int(binary[0])
        if bit == 0:
            return binaryCalc(binary[1:])
        elif bit == 1:
            return scalar + binaryCalc(binary[1:])
    except: 
        return "the input was not a string or was not only 1s and 0s"

print(binaryCalc("0"))
print(binaryCalc("1"))
print(binaryCalc("10"))
print(binaryCalc("1010"))
print(binaryCalc("1100100"))
print(binaryCalc("1100101010110"))
print(binaryCalc("123456"))
print(binaryCalc("abcd"))
#extra comment 