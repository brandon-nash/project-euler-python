"""
Solution for Project Euler Problem # 45
https://projecteuler.net/problem=45
"""
import time
import itertools
from ESieve import SieveOfErato


def main():
    # Generate a list of prime numbers up to 9999 and remove any non four-digit primes as well as
    # the three numbers we already aware of
    limit = 9999
    primeList = SieveOfErato(limit)
    filterList = [x for x in primeList if len(str(x)) == 4]
    filterList.remove(1487)
    filterList.remove(4817)
    filterList.remove(8147)

    specialNums = []
    increment = 3330

    for prime in filterList:
        permutations = set([''.join(p) for p in itertools.permutations(str(prime))])
        nextNum = prime + increment
        if nextNum in filterList and str(nextNum) in permutations:
            lastNum = nextNum + increment
            if lastNum in filterList and str(lastNum) in permutations:
                specialNums.extend([prime, nextNum, lastNum])
                break

    print 'The numbers we found are ' + str(specialNums)
    # The numbers we found are [2969, 6299, 9629]
    print 'The twelve digit combination of the numbers is ' + (str(specialNums[0]) + str(specialNums[1]) + \
                                                               str(specialNums[2]))
    # The twelve digit combination of the numbers is 296962999629

if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'