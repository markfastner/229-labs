"""
Name: Mark Fastner
CECS 229 Sec 07
Programming assignment #4
4/23/2021
"""
class Vector:

    # input: l - a list
    # Example: Vector([1, 2, 3, 4]) will make a vector <1, 2, 3, 4>
    def __init__(self, l):
        # ALREADY DONE FOR YOU! DO NOT TOUCH
        self.v = l
        self.size = len(l)

    # get's the ith element of the vector
    def get_ith_element(self, i):
        return self.v[i]

    # Part0
    # vector addition (ALREADY IMPLEMENTED)
    # inputs: self, other
    # output: if addition is possible, return the sum
    #                 if addition is not possible, return None
    def __add__(self, other):
        if self.size != other.size:
            return None
        sum = []
        for i in range(self.size):
            sum.append(self.get_ith_element(i) + other.get_ith_element(i))
        return Vector(sum)

    # Part1
    # TODO: implement vector subtraction
    # inputs: self, other
    # output: if subtraction is possible, return the differences
    #                 if subtraction is not possible, return None
    def __sub__(self, other):
        difference = []
        if self.size != other.size:
            return None
        for i in range(self.size):
            difference.append(self.get_ith_element(i) - other.get_ith_element(i))
        return Vector(difference)

    # Part2
    # TODO: implement dot product
    # inputs: self, other
    # output: if dot product is possible, return the dot product
    #                 if dot product is not possible, return None
    def __mul__(self, other):
        product = []
        if self.size != other.size:
            return None
        for i in range(self.size):
            product.append(self.get_ith_element(i) * other.get_ith_element(i))
        s = 0
        for i in product:
            s += i
        return s

    # DO NOT TOUCH! For debugging purposes
    def __str__(self):
        return str(self.v)
