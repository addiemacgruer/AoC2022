#!/usr/bin/python3

import heapq

valves = {}
with open("input16.txt") as ih:
    for l in (l.strip() for l in ih.readlines()):
        p = l.split(" ", 9)
        rate = int(p[4].split("=")[1].strip(";"))
        joins = [j for j in (p[-1].split(", "))]
        valves[p[1]] = [rate, joins]

def dijkstra(start):
    queue = []
    delta = {k: 99999 for k in valves.keys()}
    predecessors = {}
    delta[start] = 0 
    heapq.heappush(queue, (0, start))
    while queue:
        last, current = heapq.heappop(queue)
        for name in valves[current][1]:
            candidate = last + 1
            if candidate < delta[name]:
                delta[name] = candidate
                predecessors[name] = current
                heapq.heappush(queue, (candidate, name))
    return delta
dijks = {name:dijkstra(name) for name in valves.keys()}

def opener(opened,remaining,release,destination):
    if remaining <= 1 or len(opened) == len(valves):
        return (release,opened)

    if not destination in opened:
        new_opened = opened.copy()
        new_opened.add(destination)
        new_remaining = remaining - 1
        release += valves[destination][0] * new_remaining
        return opener(new_opened, new_remaining, release, destination)

    best = (release,opened)
    for dest, dist in dijks[destination].items():
        if dest in opened:
            continue
        if valves[dest][0] == 0:
            continue
        if dist > remaining - 2:
            continue
        prospective = opener(opened, remaining - dist, release, dest)
        if prospective[0] > best[0]:
            best = prospective
    return best

p1 = opener({"AA"}, 30, 0, "AA")
print("1:", p1[0]) # 1474

p2 = opener({"AA"}, 26, 0, "AA")
elephant = opener(set(p2[1]), 26, 0, "AA")
print("2:", p2[0] + elephant[0]) # 2100
