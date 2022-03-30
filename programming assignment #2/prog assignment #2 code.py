#Mark Fastner
#Prog Asignment 2
#3/19/2021

def generate_rsa_key(p, q):
    """
 returns a valid RSA key (n, e)
 INPUT:
     p, q - positive integers greater than 1
 OUTPUT:
     the key as a tuple

 """
    n = q * p
    divs = divisors((p - 1) * (q - 1))
    primes = primes_less_than((p - 1) * (q - 1))
    vals = []

    for i in primes:
        if i not in divs:
            vals.append(i)
    x = vals[2]
    return (n, x)


def primes_less_than(n):
    """
 finds all primes less than the given integer.
 INPUT:
     n - a positive integer greater than 1.
 OUTPUT:
     a list of all prime numbers less than n
 """

    list = []
    for i in range(2, n + 1):
        list.append(i)
        length = len(list)

    for i in range(len(list)):
        if i >= length:
            break
        p = list[i]
#goes through all the numbers greater then 2 until it reaches the lenght chekcs if its prime and if not removes all multiples
        while p <= n:
            if p + list[i] in list:
                list.remove(p + list[i])
            p += list[i]
            length = len(list)

    return list


def divisors(n):
    """
 returns the positive divisors of n
 INPUT:
     n - positive integer
 OUTPUT:
     list of divisors, in increasing order

 """

    divs = []
    for i in range(1, n + 1):
        if n % (i) == 0:
            divs.append(i)
    return divs


"""TESTER CELL"""
print("Testing primes_less_than(100) = ", primes_less_than(100))
print("Expected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]")
p_list = primes_less_than(10000)
print("Number of primes less than 10,000 = ", len(p_list))
print("Expected: 1229")

"""TESTER CELL"""
d = divisors(2436)
print("Testing divisors(2436) produced:", d)
print("Expected: [1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 29, 42, 58, 84, 87, 116, 174, 203, 348, 406, 609, 812, 1218, 2436]")

"""TESTER CELL"""
(n, e) = generate_rsa_key(43, 59)
print("Testing generate_rsa_key() produced: (", n, ",", e, ")")
print("Expected: (2537, 13)")
