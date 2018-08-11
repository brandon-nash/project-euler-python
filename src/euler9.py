"""
Solution for Project Euler Problem # 9
https://projecteuler.net/problem=9
"""
import time


def find_gcd(a, b):
    x, y = 0, 0

    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a

    while x % y != 0:
        temp = x
        x = y
        y = temp % x

    return y


def main():

    a, b, c = 0, 0, 0
    sum_of_abc = 1000

    m, k, n, d = 0, 0, 0, 0
    limit = int((sum_of_abc / 2)**0.5)
    found = False

    for m in range(2, limit + 1):
        if (sum_of_abc / 2) % m == 0:
            k = m + 1
        else:
            k = m + 2
        while k < (2*m) and (k <= sum_of_abc / (2*m)):
            if (sum_of_abc / (2*m) % k == 0) and find_gcd(k, m) == 1:
                d = sum_of_abc / 2 / (k*m)
                n = k - m
                a = d * (m**2 - n**2)
                b = 2*d*n*m
                c = d*(m**2 + n**2)
                found = True
                break
            k += 2
        if found:
            break

    print 'The special Pythagorean triplet is'
    print 'a = ' + str(a)  # a = 375
    print 'b = ' + str(b)  # b = 200
    print 'c = ' + str(c)  # c = 425
    print 'And the sum is ' + str(a+b+c)
    print 'The product of abc is ' + str(a*b*c)
    # The product of abc is 31875000


if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'