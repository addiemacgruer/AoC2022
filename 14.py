#!/usr/bin/python3

seg_to_tup = lambda s: tuple(int(i) for i in s.split(","))
add = lambda a,b: (a[0] + b[0], a[1] + b[1])

grid = {}
def draw_line(a, b):
    if b[0] > a[0]:
        angle = ( 1,  0)
    elif b[0] < a[0]:
        angle = (-1,  0)
    elif b[1] > a[1]:
        angle = ( 0,  1)
    elif b[1] < a[1]:
        angle = ( 0, -1)
    grid[a] = '#'
    while a != b:
        a = add(a, angle)
        grid[a] = '#'

with open("input14.txt") as ih:
    for l in (l.strip() for l in ih.readlines()):
        parts = [seg_to_tup(p) for p in l.split(" -> ")]
        a = parts[0]
        for b in parts[1:]:
            draw_line(a, b) 
            a = b

min_x = min(p[0] for p in grid.keys())
max_x = max(p[0] for p in grid.keys())
max_y = max(p[1] for p in grid.keys()) + 2

def fall(sand):
    for d in ((0,1),(-1,1),(1,1)):
        down = add(sand, d)
        if not down in grid:
            return down
    return sand
    
def fill_sand():
    while True:
        sand = (500,0)
        while True:
            if sand[1] > max_y:
                return
            sand, old = fall(sand), sand
            if sand == old:
                grid[sand] = 'O'
                if sand == (500,0):
                    return
                break

fill_sand()
print("1:", list(grid.values()).count('O')) # 665

draw_line((min_x - 200, max_y), (max_x + 200, max_y))
fill_sand()
print("2:", list(grid.values()).count('O')) # 25434
