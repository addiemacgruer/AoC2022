#!/usr/bin/python3

def undigit(d):
    if d == '2': return 2
    if d == '1': return 1
    if d == '0': return 0
    if d == '-': return -1
    if d == '=': return -2

def unsnafu(snaf):
    decimal = 0
    place = 1
    for i in range(len(snaf)-1,-1,-1):
        decimal += place * undigit(snaf[i])
        place *= 5
    return decimal

def digit(d):
    if d == 0: return '0', 0
    if d == 1: return '1', 0
    if d == 2: return '2', 0
    if d == 3: return '=', 1
    if d == 4: return '-', 1

def snafu(decimal):
    snaf = ""
    while decimal != 0:
        decimal, remainder = decimal // 5, decimal % 5 
        symbol, carry = digit(remainder)
        snaf = symbol + snaf
        decimal += carry
    return snaf

with open("input25.txt") as ih:
    print("1:",snafu(sum(unsnafu(line.strip()) for line in ih.readlines()))) # 2=20---01==222=0=0-2
