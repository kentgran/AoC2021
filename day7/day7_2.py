#!/usr/bin/env python
from collections import deque

f = open('input.txt', 'r')
count, fuel = 0, 0
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
chunks.sort()
max, min = maxmin(chunks)

crabs = len(chunks)

avg = sum(chunks) / crabs
print("gjennomsnitt: {}, max: {}, min: {}, crabs: {}".format(avg, max, min, crabs))

numlist1 = deque([0] * (max[0] + 1))
numlist2 = deque()
numlist3 = deque([0] * (max[0] + 1))
i = 0
while i < len(chunks):
    numlist1[chunks[i]] += 1
    i += 1
i = 0
j = (max[0] + 1)
while i < j:
    tmp = numlist1.popleft()
    k = 0
    while k < j:
        numlist3[k] = (numlist1[k] if k < len(numlist1) else 0) + \
                      (numlist2[k] if k < len(numlist2) else 0)
        k += 1
    k, l, energy = 0, 0, 0
    while k < j:
        l += k + 1
        energy += l * numlist3[k]
        k += 1
    if fuel == 0 or energy < fuel:
        fuel = energy
    numlist2.appendleft(tmp)
    i += 1
print("energy: {}".format(fuel))
