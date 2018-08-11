"""
Solution for Project Euler Problem #5
https://projecteuler.net/problem=5
"""


def test(num, limit):
    isDivisible = True

    for i in range(2, limit + 1):
        # We need to cast these to floats so that the precision doesn't get cut off early
        if float(num) % float(i) != float(0.0):
            return False

    # If we make it to this point, we've found the first (smallest) number evenly divisible by the #'s 1-20
    return isDivisible


def main():

    # Testing divisors from 1-20
    limit = 20

    # Since the greatest divisor is 20, we can infer that it's only possible to test numbers that are divisible by 20
    x = limit + 20
    found = False

    while not found:
        found = test(x, limit)
        x += 20

    print x # 232792560

if __name__ == '__main__':
    main()


