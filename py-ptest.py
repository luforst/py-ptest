#Title: py-primality-test
#Author: Lukas Forst
#License: MIT license

from math import sqrt

def ptest_bf(x): #bf stands for brute force
    i = 2
    if x < 2: #only positive integers are possible, 1 is neither prime nor non-prime
        return False
    while i <= round(sqrt(x)):
        if x%i == 0:
            return False
        i += 1
    return True

if __name__ == "__main__":
    numbers =[1111, 1113, 1131, 1311, 3111, 3311, 3131, 3113, 1331, 1313, 1133, 1333, 3133, 3313, 3331, 3333]
    primes = []
    print("num : prime?")
    for n in numbers:
        res = ptest_bf(n)
        print("{0}: {1}".format(n, res))

