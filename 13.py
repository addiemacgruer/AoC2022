#!/usr/bin/python3

from functools import cmp_to_key

with open("input13.txt") as ih:
	input = list(reversed([l.strip() for l in ih.readlines() if l != "\n"]))

pairs = []
while input:
    pairs.append(( eval(input.pop()), eval(input.pop()) ))

cmp = lambda l, r : (l > r) - (l < r)

def ordered(left,right):
    ll = type(left) is list
    rl = type(right) is list
    if not ll and not rl:
        return cmp(left,right)
    if ll and rl:
        for item in zip(left, right):
            c = ordered(item[0],item[1])
            if c != 0:
                return c
        return cmp(len(left), len(right))
    return ordered(left if ll else [left], right if rl else [right])

tests = (ordered(p[0], p[1]) for p in pairs)
print("1:", sum(z[0] for z in enumerate(tests,1) if z[1] == -1)) # 6395

order = [[[2]],[[6]]]
for p in pairs:
    order += p
order.sort(key = cmp_to_key(ordered))
print("2:", (order.index([[2]]) + 1) * (order.index([[6]]) + 1)) # 24921
