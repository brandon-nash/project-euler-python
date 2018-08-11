"""
Solution for Project Euler Problem # 10
https://projecteuler.net/problem=10
"""


def isPrimeNumber(num):

    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True


def main():

    # We'll start already knowing that '2' is prime. This helps simplify some clean up some calculations in 'isPrime'
    i = 3
    limit = 2000000
    runningSum = 2

    while i < limit:
        if isPrimeNumber(i):
            runningSum += i
        i += 2

    print 'Sum of all primes below two million is: ' + str(runningSum)  # Sum of all primes below two million is: 142913828922

if __name__ == '__main__':
    main()