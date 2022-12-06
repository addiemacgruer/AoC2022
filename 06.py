#!/usr/bin/python3

with open("input06.txt") as ih:
    inp = ih.readlines()[0]

def start_of_sig(un):
    for i in range(len(inp) - un):
        if len(set(inp[i : i+un])) == un:
            return i + un

print("1:", start_of_sig(4))  # 1804
print("2:", start_of_sig(14)) # 2508
