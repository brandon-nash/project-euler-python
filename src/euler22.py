"""
Solution for Project Euler Problem #22
https://projecteuler.net/problem=22
"""
import string

namesList = []

with open('names.txt', 'r') as f:
	for line in f.readlines():
		names = line.strip().split(',')
		for name in names:
			namesList.append(name)


alphabetizedList = sorted(namesList)

scoresByName = {}


for name in alphabetizedList:
	namescore = 0
	for ch in name:
		namescore += (string.uppercase.index(ch) + 1)
	namescore *= (alphabetizedList.index(name) + 1)
	scoresByName[name] = namescore

totalscore = sum(scoresByName.values())
print totalscore # 871198282
