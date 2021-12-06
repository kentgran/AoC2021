#!/usr/bin/env python

f = open('input.txt', 'r')
depth, forward, aim = 0, 0, 0

for line in f:
    line = line.replace('\n', '')
    chunks = line.split(' ')
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
print("multiply your final horizontal position by your final depth:{}".format(depth*forward))

