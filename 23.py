#!/usr/bin/python3

from collections import Counter

with open("input23.txt") as ih:
	input = [l.strip() for l in ih.readlines()]

elves = set()
for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] == '#':
            elves.add((x,y))

def count_ground():
    xmin = min(e[0] for e in elves)
    xmax = max(e[0] for e in elves)
    ymin = min(e[1] for e in elves)
    ymax = max(e[1] for e in elves)
    return (1 + xmax - xmin) * (1 + ymax - ymin) - len(elves)

adj = ((-1,-1),(-1,0),(-1,+1),(0,-1),(0,+1),(+1,-1),(+1,0),(+1,+1))
moves = [(((-1,-1),(0,-1),(+1,-1)),(0,-1)),
         (((-1,+1),(0,+1),(+1,+1)),(0,+1)),
         (((-1,-1),(-1,0),(-1,+1)),(-1,0)),
         (((+1,-1),(+1,0),(+1,+1)),(+1,0))]
add = lambda a,b: (a[0] + b[0], a[1] + b[1])

def round():
    global elves,moves
    prospective = {}

    for elf in elves:
        if not any(add(elf,a) in elves for a in adj):
            prospective[elf] = elf
            continue
        for adjs,t in moves:
            if not any(add(elf,a) in elves for a in adjs):
                prospective[elf] = add(elf,t)
                break
        else:
            prospective[elf] = elf

    for p,c in Counter(prospective.values()).items():
        if c > 1:
            for e,m in prospective.items():
                if p == m:
                    prospective[e] = e

    elves = set(prospective.values())
    moves = moves[1:] + [moves[0]]
    return any(e != m for e,m in prospective.items())

i = 1
while True:
    moved = round()
    if i == 10:
        print("1:",count_ground()) # 3780
    if not moved:
        print("2:", i) # 930
        break
    i += 1
