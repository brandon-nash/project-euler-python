"""
Solution for Project Euler Problem # 29
https://projecteuler.net/problem=29
"""
import time


def main():
    lower_bound = 2
    upper_bound = 100

    distinctNums = set([])

    for i in range(lower_bound, upper_bound + 1):
        for j in range(lower_bound, upper_bound + 1):
            distinctNums.add(i**j)

    sorted(distinctNums)
    print 'There are ' + str(len(distinctNums)) + ' distinct terms in the sequence generated!'
    # There are 9183 distinct terms in the sequence generated!

if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'