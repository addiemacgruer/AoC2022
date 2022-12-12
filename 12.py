#!/usr/bin/python3

with open("input12.txt") as ih:
    inp = [line.strip() for line in ih.readlines()]

WIDTH,HEIGHT = len(inp[0]),len(inp)

adjs = ((0,-1),(0,1),(-1,0),(1,0))

def elevation(where):
    char = inp[where[1]][where[0]]
    if char == 'S':
        return ord('a') - 1
    if char == 'E':
        return ord('z')
    return ord(char)

elevation_map = {}
for y in range(HEIGHT):
    for x in range(WIDTH):
        elevation_map[(x,y)] = elevation((x,y))

def find_S():
    for y in range(HEIGHT):
        x = inp[y].find('S')
        if x == -1:
            continue
        return (x,y)

def find_length(origin, part=1):
    been = {}
    prosp = {origin:0}
    while True:
        if not prosp:
            return 9999999
        next_prosp, prosp = prosp, {}
        for place, s in next_prosp.items():
            if inp[place[1]][place[0]] == "E":
                return s
            for adj in adjs:
                x,y = place[0] + adj[0], place[1] + adj[1]
                if (x,y) in been:
                    continue
                if x < 0 or x >= WIDTH:
                    continue
                if y < 0 or y >= HEIGHT:
                    continue
                if part == 2 and inp[y][x] == 'a':
                    continue
                if elevation_map[(x,y)] > elevation_map[place] + 1:
                    continue
                prosp[(x,y)] = s + 1
            been[place] = s

print("1:",find_length(find_S())) # 481

aa = []
for y in range(HEIGHT):
    for x in range(WIDTH):
        if inp[y][x] == 'a':
            aa.append(find_length((x,y),2))
aa.sort()
print("2:",aa[0]) # 480
