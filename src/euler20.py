"""
Solution for Project Euler Problem # 20
https://projecteuler.net/problem=20
"""

num = 100
factored = 1

for i in range(num, 0, -1):
    factored *= i

factoredAsString = str(factored)

sum = 0

for i in range(0, len(factoredAsString)):
    sum += int(factoredAsString[i])

print factored  # 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
print sum  # 648