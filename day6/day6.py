#!/usr/bin/env python

f = open('input.txt', 'r')
count = 0

for line in f:
    line = line.replace('\n', '')
    chunks = list(map(int, line.split(',')))
    j = 0
    while j < 80:
        i = 0
        while i < len(chunks):
            chunks[i] -= 1
            if chunks[i] < 0:
                chunks[i] = 6
                chunks.append(9)
            i += 1
        count += 1
        #print("after: {} days: {}".format(count, chunks))
        j += 1
lanternfish = len(chunks)

print("totalt antall lanternfish: {}".format(lanternfish))
