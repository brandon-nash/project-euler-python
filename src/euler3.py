"""
Solution for Project Euler Problem # 3
https://projecteuler.net/problem=3
"""
import time

def isPrimeNumber(num):

    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True


def findMultiples(a):
    b = 2

    if a % b == 0:
        return a / b
    else:
        found = False
        b = 3
        while not found:
            if a % b == 0:
                return a / b
            else:
                b += 2


def main():

    limit = 600851475143
    primeFactors = []
    a = limit

    while a > 1:
        c = findMultiples(a)
        if isPrimeNumber(c):
            primeFactors.append(c)
        a = c

    print max(primeFactors)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took: ' + str(time.time() - start_time) + ' secs'