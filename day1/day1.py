#!/usr/bin/env python

f = open('input.txt', 'r')
thisline, increases, decreases, same = 0, 0, 0, 0
lastline = 10000

for line in f:
    line = line.replace('\n', '')    # remove '\n' only
    thisline = int(line)
    if thisline > lastline:
        increases += 1
    lastline = thisline
f.close()
print("increases: {}".format(increases))
