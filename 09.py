#!/usr/bin/python3

with open("input09.txt") as ih:
    inp = [line.strip().split(" ") for line in ih.readlines()]

def update_tail(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return tail
    x, y = tail[0], tail[1]
    if x < head[0]:
        x += 1
    if x > head[0]:
        x -= 1
    if y < head[1]:
        y += 1
    if y > head[1]:
        y -= 1
    return (x, y)

def simulate(rope_length):
    tail = set()

    rope = []
    for i in range(rope_length):
        rope.append((0,0)) 

    for direction, count in inp:
        for _ in range(int(count)):
            if direction == "R":
                rope[0] = (rope[0][0] + 1, rope[0][1])
            if direction == "L":
                rope[0] = (rope[0][0] - 1, rope[0][1])
            if direction == "U":
                rope[0] = (rope[0][0], rope[0][1] + 1)
            if direction == "D":
                rope[0] = (rope[0][0], rope[0][1] - 1)

            for i in range(1, rope_length):
                rope[i] = update_tail(rope[i-1], rope[i])
            tail.add(rope[-1])

    return len(tail)

print("1:", simulate( 2)) # 5858
print("2:", simulate(10)) # 2602
