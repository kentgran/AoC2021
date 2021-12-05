#!/usr/bin/env python

f = open('input.txt', 'r')
count = 0
lastline = 10000
up = 0
down = 0
forward = 0
for line in f:
    line = line.replace('\n', '')    # remove '\n' only
    chunks = line.split(' ')
    count += 1
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
print("down: {} forward:{} tot:{} multi:{}".format(down, forward, count, down*forward))
