"""
Solution for Project Euler Problem # 21
https://projecteuler.net/problem=21
"""
import time
from ESieve import SieveOfErato

def getFactors(num, primeList):
    sum = 1
    p = primeList[0]
    i = 0
    n = num
    j = 0

    while (p*p <= n) and n > 1 and i < len(primeList):
        p = primeList[i]
        i+=1
        if n % p == 0:
            j = p**2
            n = n / p
            while n % p == 0:
                j = j * p
                n = n / p
            sum = sum * (j - 1) / (p - 1)

    if n > 1:
        sum *= n + 1

    return sum - num


def main():

    limit = 10000
    amicableSum = 0

    primeList = SieveOfErato(limit)

    for i in range(2, limit + 1):
        factors = getFactors(i, primeList)

        if factors > i and factors <= limit:
            subFactors = getFactors(factors, primeList)
            if subFactors == i:
                amicableSum += i + factors

    print 'The sum of all amicable numbers under 10000 is ' + str(amicableSum) # The sum of all amicable numbers under 10000 is 31626

if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'