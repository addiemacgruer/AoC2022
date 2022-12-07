#!/usr/bin/python3

with open("input07.txt") as ih:
    inp = [line.strip() for line in ih.readlines()]
inp.reverse()

root = {}
pwd = []
here = root

while inp:
    n = inp.pop()
    if n.startswith("$ cd "):
        d = n[5:]
        if d == "/":
            pwd = []
        elif d == "..":
            pwd.pop()
        else:
            pwd.append(d)
        here = root
        for d in pwd:
            here = here[d]
        continue
    if not n.startswith("$ ls"):
        raise ValueError(n)
    while inp and not inp[-1].startswith("$"):
        size, name = inp.pop().split(" ")
        if (size == "dir"):
            here[name] = {}
        else:
            here[name] = int(size) 

smalls = 0
dirs = []
def dir_size(name, dikt):
    global smalls
    size = 0
    for k,v in dikt.items():
        if type(v) is dict:
            size += dir_size(k, v)
        else:
            size += v
    dirs.append((name, size))
    if size < 100000:
        smalls += size
    return size

total = dir_size("/", root)
print("1:", smalls) # 1491614

dirs.sort(key=lambda d:d[1])
necessary = total - (70000000 - 30000000)
for name, size in dirs:
    if size > necessary:
        print("2:", size) # 6400111
        break
