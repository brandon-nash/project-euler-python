"""
Solution for Project Euler Problem #30
https://projecteuler.net/problem=30
"""
import time


def main():
    limit = 999999  # Just guessing at the limit
    nums = []

    for i in range(2, limit + 1):
        numAsString = str(i)
        currentsum = 0
        for ch in numAsString:
            currentsum += int(ch)**5
        if str(currentsum) == numAsString:
            nums.append(i)

    print 'Found ' + str(len(nums)) + ' numbers with a sum of ' + str(sum(nums)) # Found 6 numbers with a sum of 443839

if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'