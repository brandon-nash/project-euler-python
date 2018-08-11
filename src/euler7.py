"""
Solution for Project Euler Problem #7
https://projecteuler.net/problem=7
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
    count = 1
    i = 3
    prime = 2
    limit = 10001

    while count < limit:
        if isPrimeNumber(i):
            prime = i
            count += 1
        i += 2

    print '1000 1st Prime Number is: ' + str(prime)  # 104743


if __name__ == '__main__':
    main()



