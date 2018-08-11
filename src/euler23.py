"""
Solution for Project Euler Problem # 23
https://projecteuler.net/problem=23
"""
import time

def getFactors(num):
    # Given that 1 is a factor of every number
    factors = set([1])
    startbound = 0
    boundary = 0
    iterateBy = 0

    if num % 2 == 0:
        boundary = num / 2
        startbound = 2
        iterateBy = 1
    else:
        found = False
        current = 3
        while not found:
            if num == current:
                boundary = num
                startbound = current
                iterateBy = 2
                found = True
            elif num % current == 0:
                boundary = num / current
                startbound = current
                iterateBy = 2
                found = True
            else:
                current += 2

    for i in range(startbound, boundary + 1, iterateBy):
        if num % i == 0:
            factors.add(i)

    return factors

def main():

    limit = 28123
    abundantNums = []

    # Starting with the knowledge that 12 is the smallest(first) non-abundant integer
    start = 12

    # First grab all the abundant integers
    for i in range(start, limit + 1):
        factors = getFactors(i)
        if sum(factors) > i:
            abundantNums.append(i)

    runningSum = 0
    abundantNums = sorted(abundantNums)

    # Now sum up all the integers that can't be written as the sum of two abundant integers
    for i in range(1, limit + 1):

        # If the current number is <= to smallest abundant number it can't be considered
        if i > min(abundantNums):
            # If this number isn't the double sum of one number
            # ex: 12 + 12 = 24
            if (i / 2)not in abundantNums:
                numsToTest = [j for j in abundantNums if j < i]
                broken = False
                for j in range(0, len(numsToTest) - 1):
                    if numsToTest[j] + numsToTest[j+1] == i:
                        broken = True
                        break
                if not broken:
                    runningSum += i
        else:
            runningSum += i

    print 'And the sum is ' + str(runningSum)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took: ' + str((time.time() - start_time)) + ' secs'

