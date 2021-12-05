#!/usr/bin/env python

f = open('input.txt', 'r')
count = 0
depth = 0
forward = 0
aim = 0
for line in f:
    line = line.replace('\n', '')    # remove '\n' only
    chunks = line.split(' ')
    count += 1
    thislinenumber = int(chunks[1])
    thislinetxt = chunks[0]
    if thislinetxt == "down":
        aim += thislinenumber
    elif thislinetxt == "up":
        aim -= thislinenumber
    elif thislinetxt == "forward":
        forward += thislinenumber
        depth += thislinenumber*aim
    else:
        print("error!")
f.close()
print("depth: {} forward:{} tot:{} multi:{}".format(depth, forward, count, depth*forward))

