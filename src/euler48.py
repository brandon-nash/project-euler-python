"""
Solution for Project Euler Problem # 48
https://projecteuler.net/problem=48
"""
import time


def main():

    limit = 1000
    runningSum = 0

    for i in range(1, limit + 1):
        runningSum += i**i

    runningSumAsStr = str(runningSum)
    print 'The last ten digits of the sum are ' + runningSumAsStr [len(runningSumAsStr) - 10:]
    # The last ten digits of the sum are 9110846700


if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'