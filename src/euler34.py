"""
Solution for Project Euler Problem # 34
https://projecteuler.net/problem=34
"""
import time


def main():

    limit = 100000  # Guessing on the limit here
    runningSum = 0

    for i in range(3, limit + 1):
        numAsString = str(i)
        currentSum = 0
        for ch in numAsString:
            factorial = 1
            for j in range(int(ch), 0, -1):
                factorial *= j
            currentSum += factorial

        if str(currentSum) == numAsString:
            runningSum += currentSum

    print 'And the sum is ' + str(runningSum) # And the sum is 40730

if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'