"""
Solution for Project Euler Problem # 46
https://projecteuler.net/problem=46
"""
import time
from ESieve import SieveOfErato


def isGoldberg(num, primeList, twiceSquares):

    found = False
    for prime in primeList:
        diff = num - prime

        if diff in twiceSquares:
            found = True
            break

    return found


def main():
    start = 9
    limit = 10001

    # Generate the odd composite numbers up to the limit
    oddNums = range(start, limit)[::2]
    primesToLimit = SieveOfErato(limit)
    compositeNums = [x for x in oddNums if x not in primesToLimit]

    # Generate the twice squares values up to the limit
    twiceSquares = [2*(x**2) for x in range(1, limit)]

    firstBad = 0

    for num in compositeNums:
        primes = list(reversed(sorted([x for x in primesToLimit if x < num])))
        if not isGoldberg(num, primes, twiceSquares):
            firstBad = num
            break

    print 'The first number that doesn\'t match Goldberg\'s conjecture is ' + str(firstBad)
    # The first number that doesn't match Goldberg's conjecture is 5777

if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'

