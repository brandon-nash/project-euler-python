"""
Solution for Project Euler Problem #4
https://projecteuler.net/problem=4
"""

biggest = []

limit = 1000
i = 100

while i < limit:
    for x in range(i+1, limit):
        isPalindrome = lambda n: str(n) == str(n)[::-1]
        if isPalindrome(i*x):
            biggest.append((i*x))
    i += 1
print max(biggest) # 906609



