"""
Solution for Project Euler Problem # 15
https://projecteuler.net/problem=15
"""
import time


def main():
    gridSize = 20
    paths = 1

    for i in range(0, gridSize):
        paths *= (2 * gridSize) - i
        paths /= i + 1

    print 'In a 20x20 grid there are ' + str(paths) + ' possible paths' # In a 20x20 grid there are 137846528820 possible paths


if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'