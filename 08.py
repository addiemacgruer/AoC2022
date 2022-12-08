#!/usr/bin/python3

with open("input08.txt") as ih:
    inp = [line.strip() for line in ih.readlines()]

width  = len(inp[0])
height = len(inp)

def clear(tree, x, y, dx, dy):
    if dx != 0:
        while True:
            x += dx
            if x < 0 or x >= width:
                return True
            if inp[y][x] >= tree:
                return False
    else:
        while True:
            y += dy
            if y < 0 or y >= height:
                return True
            if inp[y][x] >= tree:
                return False

p1 = 0
for y in range(height):
    for x in range(width):
        tree = inp[y][x]
        if   clear(tree, x, y,  0, -1):
            p1 += 1
        elif clear(tree, x, y, -1,  0):
            p1 += 1
        elif clear(tree, x, y,  1,  0):
            p1 += 1
        elif clear(tree, x, y,  0,  1):
            p1 += 1

print("1:", p1) # 1807

def dist(tree, x, y, dx, dy):
    count = 0
    if dx != 0:
        while True:
            x += dx
            if x < 0 or x >= width:
                return count
            count += 1
            if inp[y][x] >= tree:
                return count
    else:
        while True:
            y += dy
            if y < 0 or y >= height:
                return count
            count += 1
            if inp[y][x] >= tree:
                return count

p2 = 0
for y in range(height):
    for x in range(width):
        tree = inp[y][x]
        scenic  = dist(tree, x, y,  0,-1)
        scenic *= dist(tree, x, y, -1, 0)
        scenic *= dist(tree, x, y,  1, 0)
        scenic *= dist(tree, x, y,  0, 1)
        p2 = max(scenic, p2)

print("2:", p2) # 480000
