"""
Solution for Project Euler Problem # 42
https://projecteuler.net/problem=42
"""
import time

def calcTriangleNums(limit):

    triangleNums = []

    for i in range(1, limit + 1):
        triangleNums.append((0.5*i)*(i+1))

    return triangleNums


def main():

    alphaValues = {'A': 1, 'B': 2, 'C': 3,  'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, \
                   'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,  \
                   'X': 24, 'Y': 25,  'Z': 26}

    wordList = []
    with open('../resources/p042_words.txt', 'r') as f:
        for line in f.readlines():
            words = line.strip().split(',')
            for word in words:
                wordList.append(word.strip('"'))

    # The longest word in the list, this will give us an overestimate to how many triangle numbers we need to calculate
    # out to. We'll take the longest word and calculate that length with largest value in the alphaValues dictionary
    # longestWord * (26) <-- 'Z'
    longestWord = len(max(wordList, key=len))
    limit = longestWord * max(alphaValues.values())

    triangle_numbers_range = calcTriangleNums(limit)
    triangleNumbersFound = []

    for word in wordList:
        wordValue = 0
        for letter in word:
            wordValue += alphaValues[letter]
        if wordValue in triangle_numbers_range:
            triangleNumbersFound.append(word)

    print 'Found ' + str(len(triangleNumbersFound)) + ' triangle numbers in our search!'
    # Found 162 triangle numbers in our search!

if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took ' + str(time.time() - start_time) + ' secs'