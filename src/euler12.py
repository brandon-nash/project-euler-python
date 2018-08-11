"""
Solution for Project Euler Problem # 12
https://projecteuler.net/problem=12
"""
import time


def getNumDivisors(num):
    numOfDivisors = 0
    sqrt = int(num**0.5)

    for i in range(1, sqrt + 1):
        if num % i == 0:
            numOfDivisors += 2

    if sqrt**2 == num:
        numOfDivisors -= 1

    return numOfDivisors


def main():

    num = 0
    i = 1

    while getNumDivisors(num) < 500:
        num += i
        i += 1

    print 'The first triangle number with over five hundred divisors is ' + str(num)
    # The first triangle number with over five hundred divisors is 76576500


if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'