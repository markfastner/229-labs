#Mark Fastner
#Program assignment 3
#4/15/2021

#(Problem 1.7.1)
def myFilter(l, num):
    '''
    Input:
      -L: a list of numbers
      -num: a positive integer
    Output:
      -a list of numbers not containing a multiple of num
    Examples: >>> myFilter([1,2,4,5,7],2)
      [1, 5, 7] >>> myFilter([10,15,20,25],10)
      [15, 25]
    '''
    ret = []
    for x in l:
        if x % num != 0:
            ret.append(x)
    return ret

#(Problem 1.7.2)
def my_lists(l):
    ''' >>> my_lists([1,2,4])
    [[1], [1, 2], [1, 2, 3, 4]] >>> my_lists([0,3])
    [[], [1, 2, 3]]
    '''
    ret = []
    for x in l:
        ret.append(list(range(1, x + 1)))
    return ret

#(Problem 1.7.3)
def myFunctionComposition(f, g):
    '''
    Input:
      -f: a function represented as a dictionary such that g of f exists
      -g: a function represented as a dictionary such that g of f exists
    Output:
      -a dictionary that represents a function g of f
    Examples:
      >>> f = {0:'a',1:'b'}
      >>> g = {'a':'apple','b':'banana'}
      >>> myFunctionComposition(f,g) == {0:'apple',1:'banana'}
      True

      >>> a = {'x':24,'y':25}
      >>> b = {24:'twentyfour',25:'twentyfive'}
      >>> myFunctionComposition(a,b) == {'x':'twentyfour','y':'twentyfive'}
      True
    '''
    return {x:g[f[x]] for x in f.keys()}

#(Problem 1.7.4)
def mySum(l):
    '''
    Input:
      a list L of numbers
    Output:
      sum of the numbers in L
Be sure your procedure works for the empty list.
    Examples:
      >>> mySum([1,2,3,4])
      10
      >>> mySum([3,5,10])
      18
    '''
    ret = 0
    for x in l:
        ret += x
    return ret

#(Problem 1.7.5)
def myProduct(l):
    '''
    Input:
      -L: a list of numbers
    Output:
      -the product of the numbers in L
Be sure your procedure works for the empty list.
    Examples:
      >>> myProduct([1,3,5])
      15
      >>> myProduct([-3,2,4])
      -24
    '''
    ret = 1
    for x in l:
        ret *= x
    return ret

#(Problem 1.7.6)
def myMin(l):
    '''
    Input:
      a list L of numbers
    Output:
      the minimum number in L
Be sure your procedure works for the empty list.
Hint: The value of the Python expression float('infinity') is infinity.
    Examples:
    >>> myMin([1,-100,2,3])
    -100
    >>> myMin([0,3,5,-2,-5])
    -5
    '''
    ret = float('Infinity')
    for x in l:
        if x < ret:
            ret = x
        else:
            pass
    return ret

#main funcion
if __name__ == "__main__":
    print("Testing problem 1.7.1")
    print(myFilter({1,2,3,4,5,6,7,8,9,10}, 2))#should get rid of all the evens

    print("\nTesting problem 1.7.2")
    print(my_lists({1,2,3,4,5}))#for each num in list print list counting to that number

    print("\nTesting problem 1.7.3")
    print(myFunctionComposition({0:'a', 1:'b'}, {'a':'apple', 'b':'banana'}))#g o f

    print("\nTesting problem 1.7.4")
    print(mySum({1,2,4,5,8,9}))#adds all num in list and prints

    print("\nTesting problem 1.7.5")
    print(myProduct({1, 2, 4, 5, 8, 9}))#multiplies all nums in list and prints

    print("\nTesting problem 1.7.6")
    print(myMin({1, 2, 4, 5, 8, 9}))#prints smallest num in list