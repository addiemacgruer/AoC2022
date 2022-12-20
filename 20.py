#!/usr/bin/python3

with open("input20.txt") as ih:
	input = [int(l.strip()) for l in ih.readlines()]

seq = list(zip(input,range(len(input))))
os = seq.copy()

def find_i(i):
    for j in range(len(seq)):
        if seq[j][1] == i:
            return j
    raise ValueError(i)
def find_v(i):
    for j in range(len(seq)):
        if seq[j][0] == i:
            return j
    raise ValueError(j)

def shuffle():
    global seq
    for i in range(len(input)):
        ele = find_i(i)
        rem = seq[ele]
        seq = seq[:ele] + seq[ele+1:]
        new = (rem[0] + ele) % len(seq)
        seq = seq[:new] + [rem] + seq[new:]

def answer():
    zero = find_v(0)
    p1 = [seq[(zero + x)%len(seq)][0] for x in (1000,2000,3000)]
    return sum(p1)

shuffle()
print("1:", answer()) # 16533

seq = [(i[0]*811589153, i[1]) for i in os]
for i in range(10):
    shuffle()
print("2:",answer()) # 4789999181006
