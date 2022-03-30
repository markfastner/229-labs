def binary_to_dec(bitstring):
    newstring = bitstring.replace(" ", "")
    sum = 0
    power = len(newstring) - 1;
    for element in newstring:
        sum += int(element) * 2**power
        power = power - 1
    return sum
    """
    converts the given bitstring into the decimal representation of the number.
    INPUT:
        bitstring - a string containing 0's and 1's that is the binary representation of the number
    OUTPUT:
        the decimal representation of the bitstring as an integer
    """
    pass



if __name__ == '__main__':
    """TESTER CELL"""

print("Testing binary_to_dec(\"11 0011 1001\") = ", binary_to_dec("11 0011 1001")) # your solution should support strings with spaces
print("Expected: 825")