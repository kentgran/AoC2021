#!/usr/bin/env python

f = open('input.txt', 'r')
count = 0
increases = 0
decreases = 0
one = 10000
two = 10000
three = 10000
four = 10000
samme = 0
a = 0
b = 0
for line in f:
    line = line.replace('\n', '')    # remove '\n' only
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    one = int(line)
    a = one + two + three
    b = two + three + four
    if a > b:
        increases += 1
    if a < b:
        decreases += 1
    if a == b:
        samme += 1
    four = three
    three = two
    two = one
f.close()
print("increases: {} , decreases {} , samme {}, totalt {}".format(increases,decreases, samme, increases+decreases+samme))
