#!/usr/bin/python3

with open("input18.txt") as ih:
	input = [l.strip() for l in ih.readlines()]

cubes = set()
for line in input:
    cubes.add(tuple(int(x) for x in line.split(",")))

add = lambda a,b: (a[0]+b[0], a[1]+b[1], a[2]+b[2])

sides = (
    (1,0,0),(-1,0,0),
    (0,1,0),(0,-1,0),
    (0,0,1),(0,0,-1)
)

minx = min(c[0] for c in cubes)-1
maxx = max(c[0] for c in cubes)+1
miny = min(c[1] for c in cubes)-1
maxy = max(c[1] for c in cubes)+1
minz = min(c[2] for c in cubes)-1
maxz = max(c[2] for c in cubes)+1

air = set()
flood = set()
flood.add((minx,miny,minz))
while flood:
    fs = flood.copy()
    flood.clear()
    for f in fs:
        air.add(f)
        for side in sides:
            p = add(f,side)
            if p in air or p in fs or p in cubes:
                continue
            if p[0] < minx or p[0] > maxx:
                continue
            if p[1] < miny or p[1] > maxy:
                continue
            if p[2] < minz or p[2] > maxz:
                continue
            flood.add(p)
            
surface_area = 0
exterior_surface_area = 0

for cube in cubes:
    for side in sides:
        adjacent = add(cube,side)
        if not adjacent in cubes:
            surface_area += 1
        if adjacent in air:
            exterior_surface_area += 1

print("1:", surface_area)          # 4450
print("2:", exterior_surface_area) # 2564
