#!/usr/bin/python3

with open("input01.txt") as ih:
	input = [l.strip() for l in ih.readlines()]

cals = [0]
for line in input:
	if line == "":
		cals.append(0)
	else:
		cals[-1] += int(line)
cals.sort()

print("1:", cals[-1])       #  71471
print("2:", sum(cals[-3:])) # 211189
