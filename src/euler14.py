"""
Solution for Project Euler Problem #14
https://projecteuler.net/problem=14
"""


def workit(num):
    if num % 2 == 0:
        return num / 2
    else:
        return (3 * num) + 1


def main():

    limit = 1000000

    sequences = {}

    for i in range(13, limit + 1):
        count = 0
        num = i
        while num != 1:
            ret = workit(num)
            count += 1
            if ret == 1:
                sequences[i] = count
                num = 1
            else:
                num = ret

    biggest = max(sequences.values())
    print 'Starting #' + str(max(sequences, key=sequences.get)) + ' Length of ' + str(biggest)
    # Starting #837799 Length of 524

if __name__ == '__main__':
    main()