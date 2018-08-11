"""
Function for generating a list of primes under a limit.
 'Sieve of Eratosthenes' algorithm
Based on http://www.mathblog.dk/sum-of-all-primes-below-2000000-problem-10/
"""
def SieveOfErato(limit):
    bound = int((limit - 1) / 2)
    upperSqrt = int((limit**0.5 - 1) / 2)

    PrimeBits = [True] * (bound + 1)

    for i in range(1, upperSqrt + 1):
        if PrimeBits[i]:
            for j in range((i*2*(i+1)), bound + 1, (2*i) + 1):
                PrimeBits[j] = False

    nums = [2]

    for i in range(1, bound + 1):
        if PrimeBits[i]:
            nums.append((2*i)+1)

    return nums
