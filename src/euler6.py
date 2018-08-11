"""
Solution for Project Euler Problem # 6
https://projecteuler.net/problem=6
"""

sumOfSquares = 0
squareOfSums = 0

limit = 100

for i in range(1, limit + 1):
    sumOfSquares += i**2
    squareOfSums += i

squareOfSums = squareOfSums**2

print 'Sum of Squares: ' + str(sumOfSquares)
print 'Square of Sums: ' + str(squareOfSums)
print 'Diff = ' + str(squareOfSums - sumOfSquares) # 25164150