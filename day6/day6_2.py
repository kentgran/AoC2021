#!/usr/bin/env python

from collections import deque

f = open('input.txt', 'r')
numlist = deque([0] * 9)

for line in f:
    line = line.replace('\n', '')
    chunks = list(map(int, line.split(',')))
    i = 0
    while i < len(chunks):
        numlist[chunks[i]] += 1
        i += 1
days = 0
while days < 256:
    numlist.rotate(-1)
    numlist[6] += numlist[8]
    days += 1
print("totalt: {} lanternfish".format(sum(numlist)))