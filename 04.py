#!/usr/bin/python3

with open("input04.txt") as ih:
	input = [l.strip() for l in ih.readlines()]
	
def split(i):
	f,s = i.split(',')
	a,b = [int(n) for n in f.split('-')]
	c,d = [int(n) for n in s.split('-')]
	return ((a,b),(c,d))
	
ss = [split(i) for i in input]

t1 = 0
for s in ss:
	if s[0][0] <= s[1][0]:
		if s[0][1] >= s[1][1]:
			t1 += 1
			continue
	if s[0][0] >= s[1][0]:
		if s[0][1] <= s[1][1]:
			t1 += 1
print("1:", t1) # 651

t2 = 0
for s in ss:
	if s[0][0] <= s[1][1]:
		if s[0][1] >= s[1][0]:
			t2 += 1
			continue
	if s[0][0] <= s[1][0]:
		if s[0][1] >= s[1][1]:
			t2 += 1
print("2:", t2) # 956
	
