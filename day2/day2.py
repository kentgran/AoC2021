#!/usr/bin/env python

f = open('input.txt', 'r')
lastline = 10000
up, down, forward = 0, 0, 0

for line in f:
    line = line.replace('\n', '')
    chunks = line.split(' ')
    thislinenumber = int(chunks[1])
    thislinetxt = chunks[0]
    if thislinetxt == "down":
        down += thislinenumber
    elif thislinetxt == "up":
        down -= thislinenumber
    elif thislinetxt == "forward":
        forward += thislinenumber
    else:
        print("error!")
f.close()
print("multi:{}".format(down*forward))
