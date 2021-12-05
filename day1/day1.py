#!/usr/bin/env python

f = open('input.txt', 'r')
count = 0
lastline = 10000
thisline = 0
increases = 0
decreases = 0
samme = 0
for line in f:
    line = line.replace('\n', '')    # remove '\n' only
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    thisline = int(line)
    if thisline > lastline:
        increases += 1
    if lastline > thisline:
        decreases += 1
    if lastline == thisline:
        samme += 1
    lastline = thisline
f.close()
print("increases: {} , decreases {} , samme {}, totalt {}".format(increases,decreases, samme, increases+decreases+samme))
