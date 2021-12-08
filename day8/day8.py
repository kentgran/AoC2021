#!/usr/bin/env python

f = open('input.txt', 'r')
count = 0
chunks = []
result = []
instances = 0


for line in f:
    line = line.replace('\n', '')
    chunks = line.split('| ')
    result = chunks[1].split(' ')
    for rad in result:
        lengde = len(rad)
        if lengde in [2,3,4,7]:
            instances+=1
    count += 1

print("instanser: {}".format(instances))