"""
Solution for Project Euler Problem # 45
https://projecteuler.net/problem=45
"""
import time


def main():
    start = 286
    limit = 100000  # Guessing at the limit here

    triangleNums = {}
    pentagonalNums = {}
    hexagonalNums = {}

    for i in range(1, limit):
        triangleNums[i] = i*(i + 1)/2
        pentagonalNums[i] = i*(3*i - 1)/2
        hexagonalNums[i] = i*(2*i - 1)

    # Delete the first occurrences that we're aware of
    del (triangleNums[285])
    del (triangleNums[1])
    del (pentagonalNums[165])
    del (pentagonalNums[1])
    del (hexagonalNums[143])
    del (hexagonalNums[1])

    triangleValue = 0

    for num in triangleNums.values():
        if num in pentagonalNums.values():
            if num in hexagonalNums.values():
                triangleValue = num
                break

    print 'The next triangle number that is also pentagonal and hexagonal is ' + str(triangleValue)
    # The next triangle number that is also pentagonal and hexagonal is 1533776805


if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'