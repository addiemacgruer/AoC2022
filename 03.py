#!/usr/bin/python3

with open("input03.txt") as ih:
	input = [l.strip() for l in ih.readlines()]
	
def score(prs):
	tot = 0
	for pr in prs:
		if pr >= 'A' and pr <= 'Z':
			tot += ord(pr) - ord('A') + 27
		else:
			tot += ord(pr) - ord('a') + 1
	return tot

prs = []

for i in input:
	h = int(len(i)/2)
	a,b = set(i[:h]), set(i[h:])
	pr = a.intersection(b)
	prs.append(list(pr)[0])
		
print("1:", score(prs)) # 7795

prs=[]
for i in range(len(input)//3):
	o = i*3
	a = set(input[o])
	b = set(input[o+1])
	c = set(input[o+2])
	pr = a.intersection(b).intersection(c)
	prs.append(list(pr)[0])
		
print("2:", score(prs)) # 2703
