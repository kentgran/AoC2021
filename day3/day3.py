#!/usr/bin/env python

biter = [0] * 12
j = [""] * 12
k = [""] * 12

f = open('input.txt', 'r')
count = 0
up = 0
down = 0
forward = 0
for line in f:
    line = line.replace('\n', '')    # remove '\n' only
    chunks = list(line)
    count += 1
    i = 0
    while i < 12:
        biter[i] += int(chunks[i])
        i += 1
f.close()
i = 0

while i < 12:
    j[i] = "1" if biter[i] > count/2 else "0"
    k[i] = "1" if biter[i] < count/2 else "0"
    print("bit {}: {} {}".format(i, j[i], biter[i]))
    i += 1
gamma = int("".join(j), 2)
epsilon = int("".join(k), 2)
print("gamma  : {} , {}".format("".join(j), int("".join(j), 2)))
print("epsilon: {} , {}".format("".join(k), int("".join(k), 2)))
print("multiplisert: {}".format(gamma*epsilon))
