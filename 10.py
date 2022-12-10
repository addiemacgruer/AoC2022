#!/usr/bin/python3

with open("input10.txt") as ih:
    inp = [line.strip().split(" ") for line in ih.readlines()]
inp.reverse()

x = 1
cycle = 1
signal = []

def signal_strength(cyc, x):
    if (cyc - 20) % 40 == 0:
        signal.append(cyc * x)

def print_pixel(cyc, x):
    xoffs = (cyc - 1) % 40
    if abs(xoffs - x) <= 1:
        print('#', end='')
    else:
        print('.', end='')
    if cyc % 40 == 0:
        print()

def tick(add = 0):
    global cycle, x
    print_pixel(cycle, x)
    cycle += 1
    x += add
    signal_strength(cycle, x)
    
while inp:
    ins = inp.pop()
    if ins[0] == "addx":
        tick()
        tick(int(ins[1]))
    elif ins[0] == "noop":
        tick()
    else:
        raise ValueError(ins)

print("1:", sum(signal)) # 12540 / FECZELHE
