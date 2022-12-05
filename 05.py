#!/usr/bin/python3

def read_file():
    with open("input05.txt") as ih:
        inp = [l.strip("\n") for l in ih.readlines()]

    start = inp.index("") - 1
    width = (len(inp[0]) - 1) // 4 + 1

    stacks = []
    for i in range(width):
        stack = []
        for l in inp[:start]:
            off = 4 * i + 1
            if l[off] != " ":
                stack.insert(0, l[off])
        stacks.append(stack)

    moves = []
    for line in inp[start+2:]:
        s = line.split(" ")
        moves.append((int(s[1]), int(s[3])-1, int(s[5])-1))

    return stacks, moves

def print_stacks(stacks):
    for s in stacks:
        print(s[-1], end="")
    print()

def part_1(stacks, moves):
    for m in moves:
        for count in range(m[0]):
            stacks[m[2]].append(stacks[m[1]].pop())
    print_stacks(stacks)

def part_2(stacks,moves):
    for m in moves:
        src = stacks[m[1]]
        stacks[m[1]], pick = src[:-m[0]], src[-m[0]:]
        stacks[m[2]] += pick
    print_stacks(stacks)
        
part_1(*read_file()) # QGTHFZBHV
part_2(*read_file()) # MGDMPSZTM
