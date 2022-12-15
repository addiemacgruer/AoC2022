#!/usr/bin/python3

from multiprocessing import cpu_count, Process

# p1_line, p2_range, file = 10, 20, "input15.tst"
p1_line, p2_range, file = 2000000, 4000000, "input15.txt"

point = lambda s: tuple(int(p[2:]) for p in s.split(", "))
manhattan = lambda a,b: abs(a[0] - b[0]) + abs(a[1] - b[1])
tuning_frequency = lambda p: p[0] * 4000000 + p[1]

grid = {}
with open(file) as ih:
    for a,b in (line.strip().split(": ") for line in ih.readlines() if line != "\n"):
        sensor, beacon = point(a[10:]), point(b[21:])
        grid[sensor] = manhattan(sensor, beacon)

def find_coverage(line):
    overlaps = []
    for sensor,man in grid.items():
        length = man - abs(sensor[1] - line)
        if length >= 0:
            overlaps.append([sensor[0] - length, sensor[0] + length])
    overlaps.sort()
    last = overlaps[0]
    stack = [last]
    for over in overlaps[1:]:
        if last[0] <= over[0] <= last[1] or last[1] + 1 == over[0]:
            last[1] = max(last[1], over[1])
        else:
            stack.append(over)
            last = over
    return stack
    
overlap = find_coverage(p1_line)[0]
print("1:", overlap[1] - overlap[0]) # 6124805

cpus = cpu_count()
def check_y(start):
    for y in range(start,p2_range,cpus):
        overlaps = find_coverage(y)
        if len(overlaps) > 1:
            print("2:", tuning_frequency((overlaps[0][1]+1, y))) # 12555527364986
            break
[Process(target=check_y,args=(i,)).start() for i in range(cpus)]
