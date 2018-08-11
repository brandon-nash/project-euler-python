"""
Solution for Project Euler Problem #2
https://projecteuler.net/problem=2
"""

limit = 4000000
runningSum = 0

a = 0
b = 1

fibnums = []

while b < limit:
    c = a + b
    if c % 2 == 0:
        fibnums.append(c)
    a = b
    b = c

print sum(fibnums)  # 4613732



