#!/usr/bin/python3

def make_map(pattern):
    mmap = {}
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            mmap[(x,y)] = pattern[y][x]
    return mmap

if False:
    fname = "input22.tst"
    mapping = make_map(["0010","2340","0056"])
    cube = 4
else:
    fname = "input22.txt"
    mapping = make_map(["a12","b3c","45d","6ef"])
    cube = 50

with open(fname) as ih:
	input = [l.strip("\n") for l in ih.readlines()]

board = input[:-2]
WIDTH, HEIGHT = len(board[0]), len(board)

inst = []
wip = ""
for char in input[-1]:
    if char == "L" or char == "R":
        inst.append(int(wip))
        wip = ""
        inst.append(char)
    else:
        wip += char
inst.append(int(wip)) 
    
facings = ((1,0),(0,1),(-1,0),(0,-1))

password = lambda a,b: 1000 * (a[1] + 1) + 4 * (a[0] + 1) + b

def find_next1(start,facing):
    addition = facings[facing]
    x, y = start[0], start[1]
    while True:
        x,y = (x + addition[0]) % WIDTH, (y + addition[1]) % HEIGHT
        if len(board[y]) <= x:
            continue
        if board[y][x] != " ":
            break
    if board[y][x] == ".":
        return (x,y),facing
    return start,facing

map_face = lambda x,y: mapping[(x//cube,y//cube)]

def move14(a,b,f): return 0, 149 - a[1], 0
def move16(a,b,f): return 0, 100 + a[0], 0
def move23(a,b,f): return 99, a[0] - 50, 2 
def move25(a,b,f): return 99, 149 - a[1], 2
def move26(a,b,f): return a[0] - 100, 199, 3
def move32(a,b,f): return a[1] + 50, 49, 3
def move34(a,b,f): return a[1] - 50, 100, 1
def move41(a,b,f): return 50, 149 - a[1], 0
def move43(a,b,f): return 50, a[0] + 50, 0
def move52(a,b,f): return 149, 149 - a[1], 2
def move56(a,b,f): return 49, 100 + a[0], 2
def move61(a,b,f): return a[1] - 100, 0, 1
def move62(a,b,f): return a[0] + 100, 0, 1
def move65(a,b,f): return a[1] - 100, 149, 3
def okay(a,b,f):   return b[0],b[1],f

transitions = {
    ('1','2'): okay,
    ('1','3'): okay,
    ('1','a'): move14,
    ('1','e'): move16,
    ('2','1'): okay,
    ('2','a'): move25,
    ('2','c'): move23,
    ('2','f'): move26,
    ('3','1'): okay,
    ('3','5'): okay,
    ('3','b'): move34,
    ('3','c'): move32,
    ('4','5'): okay,
    ('4','6'): okay,
    ('4','b'): move43,
    ('4','d'): move41,
    ('5','3'): okay,
    ('5','4'): okay,
    ('5','d'): move52,
    ('5','e'): move56,
    ('6','4'): okay,
    ('6','a'): move62,
    ('6','e'): move65,
    ('6','f'): move61
}

def find_next2(start,facing):
    x, y = start[0], start[1]
    face = map_face(x,y)

    addition = facings[facing]
    x_,y_ = (x + addition[0]) % WIDTH, (y + addition[1]) % HEIGHT
    face_ = map_face(x_,y_)

    move = (face,face_)
    if face == face_:
        x,y = x_,y_
    elif move in transitions:
        x,y,facing = transitions[move]((x,y),(x_,y_),facing)
    else:
        print("Can't move from ",face,"to",face_)
        raise ValueError("bad move")

    if board[y][x] == ".":
        return (x,y),facing
    return start,facing
     
def solve(nexter):
    place = (board[0].find("."), 0)
    facing = 0
    for i in inst:
        if i == "L":
            facing = (facing - 1) % len(facings)
            continue
        if i == "R":
            facing = (facing + 1) % len(facings)
            continue
        for j in range(i):
            next_place,next_facing = nexter(place,facing)
            if place != next_place:
                place,facing = next_place,next_facing
            else:
                break
    return password(place,facing)

print("1:", solve(find_next1)) # 55244
print("2:", solve(find_next2)) # 123149
