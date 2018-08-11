"""
Solution for Project Euler Problem #24
https://projecteuler.net/problem=24
"""
import time


def permutate(number):

    permutations = []

    if len(number) == 2:
        permutations.append(number[0] + number[1])
        permutations.append(number[1] + number[0])
        return permutations
    else:
        for num in number:
            returns = [i for i in number if i != num]
            perms = permutate(returns)

            for i in range(0, len(perms)):
                permutations.append(num + perms[i])

    return permutations


def main():

    num = '0123456789'
    permutations = sorted(permutate(num))

    print 'There are ' + str(len(permutations)) + ' permutations'
    print 'The one-millionth lexicographic permuation of \'0123456789\' is ' + permutations[999999]
    # The one-millionth lexographic permuation of '0123456789' is 2783915460


if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'