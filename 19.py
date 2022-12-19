#!/usr/bin/python3

import multiprocessing

with open("input19.txt") as ih:
	input = [l.strip() for l in ih.readlines()]

class Blueprint:
    def __repr__(self):
        return ",".join(str(x) for x in (self.bp,self.ore,self.clay,self.obs,self.geo,self.max))

line = input[0]
blueprints = []
for line in input:
    blue = Blueprint()
    p = line.split(" ")
    blue.bp = int(p[1].strip(":"))
    blue.ore = (int(p[6]),0,0,0)
    blue.clay= (int(p[12]),0,0,0)
    blue.obs = (int(p[18]),int(p[21]),0,0)
    blue.geo = (int(p[27]),0,int(p[30]),0)
    blue.max = (
        max(blue.ore[0], blue.clay[0], blue.obs[0], blue.geo[0]),
        max(blue.ore[1], blue.clay[1], blue.obs[1], blue.geo[1]),
        max(blue.ore[2], blue.clay[2], blue.obs[2], blue.geo[2])
    )
    blueprints.append(blue)

sufficient = lambda cost,res: all(i[0] <= i[1] for i in zip(cost, res))
consume = lambda cost,res: [i[1]-i[0] for i in zip(cost,res)]

def calculate(bp,LIMIT):
    memo = {}
    bestg = [0] * (LIMIT + 1)
    def build(bp,robots,resources,minute=1):

        if resources[3] > bestg[minute]:
            bestg[minute] = resources[3]
        elif bestg[minute] > resources[3] + 1:
            return 0

        key = (tuple(robots),tuple(resources),minute)
        if key in memo:
            return memo[key]

        if minute == LIMIT:
            return resources[3]

        res = resources.copy()
        res[0] += robots[0] # ore
        res[1] += robots[1] # clay
        res[2] += robots[2] # obs
        res[3] += robots[3] # geode

        next_turn = []

        # build geo?
        if                           minute < LIMIT - 1 and sufficient(bp.geo,resources):
            next_turn.append((
                [robots[0],robots[1],robots[2],robots[3]+1],
                consume(bp.geo, res)
            ))
        # build obs?
        if robots[2] < bp.max[2] and minute < LIMIT - 2 and sufficient(bp.obs,resources):
            next_turn.append((
                [robots[0],robots[1],robots[2]+1,robots[3]],
                consume(bp.obs, res)
            ))
        # build clay?
        if robots[1] < bp.max[1] and minute < LIMIT - 3 and sufficient(bp.clay,resources):
            next_turn.append((
                [robots[0],robots[1]+1,robots[2],robots[3]],
                consume(bp.clay, res)
            ))
        # build ore?
        if robots[0] < bp.max[0] and minute < LIMIT - 4 and sufficient(bp.ore,resources):
            next_turn.append((
                [robots[0]+1,robots[1],robots[2],robots[3]],
                consume(bp.ore, res)
            ))
        next_turn.append((robots,res)) # do nothing

        best = 0
        for nexts in next_turn:
            best = max(best,build(bp,nexts[0],nexts[1],minute+1))

        memo[key] = best

        return best
    return build(bp,[1,0,0,0],[0,0,0,0])

def part_1(bp): return bp.bp * calculate(bp,25)
def part_2(bp): return calculate(bp,33)

with multiprocessing.Pool() as pool:
    results = pool.map(part_1, blueprints)
print("1:", sum(results))

with multiprocessing.Pool() as pool:
    results = pool.map(part_2, blueprints[0:3])
part2 = 1
for r in results:
    part2 *= r
print("2:",part2) # 19980
