#!/usr/bin/python3

with open("input21.txt") as ih:
	input = [l.strip() for l in ih.readlines()]

monkeys = {}
for line in input:
    monkey,m = line.split(": ")
    math = m.split(" ")
    if len(math) == 1:
        monkeys[monkey] = int(math[0])
    else:
        monkeys[monkey] = math

def evaluate(m):
    math = monkeys[m]
    if type(math) is str:
        return (math,)
    if type(math) is int:
        return math

    first = evaluate(math[0])
    op = math[1]
    second = evaluate(math[2])

    if type(first) is tuple or type(second) is tuple:
        return (first,op,second)

    if op == "+":
        return first + second
    if op == "-":
        return first - second
    if op == "*":
        return first * second
    if op == "/":
        return first // second
    if op == "=":
        return first == second

print("1:", evaluate("root"))

monkeys["root"][1] = "="
monkeys["humn"] = "humn"

def solve(eqn):
    ans = eqn[2]
    eqn = eqn[0]
    while True:
        if len(eqn) == 1:
            break
        lhs = eqn[0]
        rhs = eqn[2]
        op = eqn[1]
        if op == "*":
            if type(lhs) is int:
                ans //= lhs
                eqn = rhs
                continue
            if type(rhs) is int:
                ans //= rhs
                eqn = lhs
                continue
        if op == "/":
            if type(rhs) is int:
                ans *= rhs
                eqn = lhs
                continue
        if op == "+":
            if type(lhs) is int:
                ans -= lhs
                eqn = rhs
                continue
            if type(rhs) is int:
                ans -= rhs
                eqn = lhs
                continue
        if op == "-":
            if type(lhs) is int:
                eqn = rhs
                ans = lhs - ans
                continue
            if type(rhs) is int:
                eqn = lhs
                ans += rhs
                continue
        raise ValueError("whoops!")
    return eqn,"=",ans

print("2:",solve(evaluate("root"))) # 3910938071092
