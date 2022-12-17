#!/usr/bin/python3

with open("input17.txt") as ih:
	input = [l.strip() for l in ih.readlines()][0]

rocks = [list(reversed(r.split("\n"))) for r in (
"####",
".#.\n###\n.#.",
"..#\n..#\n###",
"#\n#\n#\n#",
"##\n##"
)]

rock_size = [(len(rock[0]),len(rock)) for rock in rocks]
chamber = set()
add = lambda a,b: (a[0] + b[0], a[1] + b[1])
max_depth = lambda: max(c[1] for c in chamber) + 1 if chamber else 0

def can_move(rock_i,offs):
    size = rock_size[rock_i]
    rock = rocks[rock_i]
    for y in range(size[1]):
        for x in range(size[0]):
            pos = add(offs,(x,y))
            if pos[0] < 0 or pos[0] >= 7:
                return False
            if pos[1] < 0:
                return False
            if rock[y][x] == '#':
                if add(offs,(x,y)) in chamber:
                    return False
    return True

def place(rock_i,offs):
    size = rock_size[rock_i]
    rock = rocks[rock_i]
    for y in range(size[1]):
        for x in range(size[0]):
            if rock[y][x] == '#':
                chamber.add(add(offs,(x,y)))

def clear_out():
    global chamber
    limit = max_depth() - 50
    new_chamber = set()
    for entry in chamber:
        if entry[1] > limit:
            new_chamber.add(entry)
    chamber = new_chamber

def drop_rocks(total):
    gust = 0
    drop = 0
    repeats = {}
    repeat_skip = 0
    while drop < total:
        rock_i = drop % len(rocks)
        rock = rocks[rock_i]
        gust_i = gust % len(input)

        # loop detection
        if (drop % 1000) == 0:
            clear_out()
            key = (rock_i, gust_i)
            if key in repeats:
                previous = repeats[key]
                interval = drop - previous[0]
                count = max_depth() - previous[1]
                repeat_count = ((total - previous[1]) // interval) - 1
                total -= interval * repeat_count
                repeat_skip = count * repeat_count
                repeats.clear()
            else:
                repeats[key] = (drop,max_depth())

        # drop it
        offs = (2,max_depth() + 3)
        while True:
            gust_i = gust % len(input)
            motion = input[gust_i]
            gust += 1
            if motion == ">":
                new_offs = add(offs,(1,0))
                if can_move(rock_i,new_offs):
                    offs = new_offs
            elif motion == "<":
                new_offs = add(offs,(-1,0))
                if can_move(rock_i,new_offs):
                    offs = new_offs
            else:
                raise ValueError(motion)
            new_offs = add(offs,(0,-1))
            if not can_move(rock_i,new_offs):
                break
            offs = new_offs
        place(rock_i,offs)
        drop += 1
    return max_depth() + repeat_skip

print("1:", drop_rocks(2022))         # 3111
chamber.clear()
print("2:",drop_rocks(1000000000000)) # 1526744186042
