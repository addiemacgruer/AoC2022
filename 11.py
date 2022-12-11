#!/usr/bin/python3

def do_part(part):
    monkeys = []
    modulo = 1
    class Monkey:
        inspects = 0

        def turn(self):
            for old in self.items:
                self.inspects = self.inspects + 1
                rhs = old if self.operation[2] == "old" else int(self.operation[2])
                if self.operation[1] == "+":
                    new = old + rhs
                else:
                    new = old * rhs

                if part == 1:
                    new //= 3
                else:
                    new %= modulo

                if new % self.test == 0:
                    monkeys[self.true].items.append(new)
                else:
                    monkeys[self.false].items.append(new)
                 
            self.items = []

    with open("input11.txt") as ih:
        inp = list(reversed([line.strip() for line in ih.readlines()]))

    while inp: 
        l = inp.pop() 
        if l.startswith("Monkey"):
            monkeys.append(Monkey())
        elif l.startswith("Starting items"):
            monkeys[-1].items = [int(x) for x in l.split(": ")[1].split(", ")]
        elif l.startswith("Operation"):
            monkeys[-1].operation = l.split(" = ")[1].split(" ")
        elif l.startswith("Test: "):
            monkeys[-1].test = int(l.split(" ")[-1])
        elif l.startswith("If true:"):
            monkeys[-1].true = int(l.split(" ")[-1])
        elif l.startswith("If false:"):
            monkeys[-1].false = int(l.split(" ")[-1])
        elif l == "":
            pass

    if part == 2:
        for m in monkeys:
            modulo *= m.test

    for _ in range(20 if part==1 else 10000):
        [monkey.turn() for monkey in monkeys]

    inspects = sorted([m.inspects for m in monkeys])
    print(part,":",inspects[-2] * inspects[-1])

do_part(1) # 61005
do_part(2) # 20567144694
