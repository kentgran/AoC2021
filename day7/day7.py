#!/usr/bin/env python

f = open('testinput.txt', 'r')
count = 0
chunks = []

def maxmin(_listen):
    k = 0
    _max = [0, 0]
    _min = [1000000, 0]
    _elements = len(_listen)
    while k < _elements:
        if _listen[k] < _min[0]:
            _min[0] = _listen[k]
            _min[1] = k
        if _listen[k] > _max[0]:
            _max[0] = _listen[k]
            _max[1] = k
        k += 1
    return _max, _min


for line in f:
    line = line.replace('\n', '')
    chunks = list(map(int, line.split(',')))
    count += 1
max, min = maxmin(chunks)

crabs = len(chunks)


avg = sum(chunks) / crabs

j = min[0]
fuel = [0] * (max[0] - min[0])
while j < max[0]:
    i = 0
    while i < crabs:
        dist = abs(j - chunks[i])
        fuel[j - min[0]] += dist
        i += 1
    j += 1

maxfuel, minfuel = maxmin(fuel)

print("gjennomsnitt: {}, max: {}, min: {}, crabs: {}".format(avg, max, min, crabs))
print("maxfuel: {} ({}) minfuel: {} ({})".format(maxfuel[0], maxfuel[1], minfuel[0], minfuel[1]))