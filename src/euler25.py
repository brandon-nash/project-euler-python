"""
Solution for Project Euler Problem # 25
https://projecteuler.net/problem=25
"""
import time


def main():
    a = 0
    b = 1
    index = 1
    found = False

    while not found:
        index += 1
        c = a + b
        a = b
        b = c
        if len(str(c)) == 1000:
            found = True


    print 'And the index with the first 1000 thousand digit fibonacci number (' + str(b) + ') is ' + str(index) # 4782

if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'