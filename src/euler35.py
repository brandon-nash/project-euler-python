"""
Solution for Project Euler Problem # 35
https://projecteuler.net/problem=35
"""
import time
import itertools
from ESieve import SieveOfErato


def isPrimeNumber(num):

    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True


def permutate(number):

    permutations = []

    if len(number) == 2:
        permutations.append(number[0] + number[1])
        permutations.append(number[1] + number[0])
        return permutations
    else:
        for num in number:
            returns = [i for i in number if i != num]
            perms = permutate(returns)

            for i in range(0, len(perms)):
                permutations.append(num + perms[i])

    return permutations


def main():
    #limit = 1000000
    limit = 999331
    circularPrimes = set([])

    # Using the SieveOfErato function, we'll generate the list of primes up to one-million
    primeList = SieveOfErato(limit)

    # Remove any prime numbers containing 2, 4, 5, 6, 8. Eventually there will be a permutation that will
    # not be prime for these numbers
    primeList = sorted([num for num in primeList if '2' not in str(num) and '4' not in str(num) and '6' not in str(num) and '8' not in
                 str(num) and '5' not in str(num)])

    # But we do want 2 and 5 to be in the list so add those to the list
    circularPrimes.add(2)
    circularPrimes.add(5)

    for prime in primeList:
        permutations = set([''.join(p) for p in itertools.permutations(str(prime))])
        permutationsAsInt = [int(x) for x in permutations]
        isCircular = True

        for perm in permutationsAsInt:
            #if perm not in primeList:
            #    isCircular = False
            #    break
            if not isPrimeNumber(perm):
                isCircular = False
                break

        if isCircular:
            circularPrimes |= set(permutationsAsInt)

    print 'Found ' + str(len(circularPrimes)) + ' circular primes under one-million'
    print sorted(circularPrimes)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'