
def gcd(a, b):
    """returns the gcd of integers a and b
    INPUT:
        a, b - integers
    OUTPUT:
        the gcd as an int

    """
    r = 0;

    while True:
        r = a % b;
        if r == 0 :
            return b;
            break;

        a = b;
        b = r;

    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """TESTER CELL"""

    print("Testing gcd(101, 4620) = ", gcd(101, 4620))
    print("Expected: 1")
    print("Testing gcd(2349, 36) = ", gcd(2349, 36))
    print("Expected: 9")
