"""
Solution for Project Euler Problem #1
https://projecteuler.net/problem=1
"""
limit = 1000

runningsum = 0

for i in range(1, limit):
    if i % 3 == 0 or i % 5 == 0:
        runningsum += i

print runningsum # 233168
