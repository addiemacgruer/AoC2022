#!/usr/bin/python3

with open("input24.txt") as ih:
	input = [l.strip() for l in ih.readlines()]

blizzard = {}
WIDTH, HEIGHT = len(input[0]), len(input)
START, END = (1,0), (WIDTH-2,HEIGHT-1)

dirs={'v': ( 0,  1),
      '>': ( 1,  0),
      '<': (-1,  0),
      '^': ( 0, -1)}

for y in range(1,HEIGHT-1):
    for x in range(1,WIDTH-1):
        c = input[y][x]
        if c != '.':
            blizzard[(x,y)] = dirs[c]

def map_at_time(time):
    mapp = set()
    for y in range(HEIGHT):
        mapp.add((0,y))
        mapp.add((WIDTH-1,y))
    for x in range(2,WIDTH-1):
        mapp.add((x,0))
    for x in range(1,WIDTH-3):
        mapp.add((x,HEIGHT-1))
    for b,s in blizzard.items():
        x = ((b[0] + s[0] * time) - 1) % (WIDTH - 2) + 1
        y = ((b[1] + s[1] * time) - 1) % (HEIGHT- 2) + 1
        mapp.add((x,y))
    return mapp

moves1 = ((0,1), (1,0), (0,0), (0,-1), (-1,0))
moves2 = tuple(reversed(moves1))

def solve(starttime,moveset,start,goal):
    best = 700
    dupes = []
    cache = []

    def walk(route):
        route_length = len(route)
        while route_length >= len(cache):
            cache.append(map_at_time(starttime + len(cache)))
            dupes.append(set())

        dupes[route_length-1].add(route[-1])

        nonlocal best
        if route_length >= best:
            return None

        position = route[-1]
        if position == goal:
            best = route_length
            return route

        mapp = cache[route_length]
        shortest = None
        for m in moveset:
            prosp = (position[0] + m[0], position[1] + m[1])
            if prosp in dupes[route_length]:
                continue
            if prosp[1] < 0 or prosp[1] >= HEIGHT:
                continue
            if not (prosp[0],prosp[1]) in mapp:
                w = walk(route + [prosp])
                if w != None:
                    shortest = w
        return shortest

    return starttime + len(walk([start])) - 1

p1 = solve(0, moves1, START, END)
print("1:",p1) # 260

p2a = solve(p1, moves2, END, START)
p2b = solve(p2a,moves1, START, END)
print("2:",p2b) # 747
