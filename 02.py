#!/usr/bin/python3

with open("input02.txt") as ih:
	input = [l.strip() for l in ih.readlines()]

scores = {
	"A X": 1+3,
	"A Y": 2+6,
	"A Z": 3+0,
	"B X": 1+0,
	"B Y": 2+3,
	"B Z": 3+6,
	"C X": 1+6,
	"C Y": 2+0,
	"C Z": 3+3,
}

print("1:", sum(scores[r] for r in input)) # 14297

scores = {
	"A X": 3+0,
	"A Y": 1+3,
	"A Z": 2+6,
	"B X": 1+0,
	"B Y": 2+3,
	"B Z": 3+6,
	"C X": 2+0,
	"C Y": 3+3,
	"C Z": 1+6,
}

print("2:", sum(scores[r] for r in input)) # 10498
