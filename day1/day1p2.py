#!/usr/bin/env python

f = open('input.txt', 'r')
increases, a, b = 0, 0, 0
one = 10000
two = 10000
three = 10000
four = 10000

for line in f:
    line = line.replace('\n', '')
    one = int(line)
    a = one + two + three
    b = two + three + four
    if a > b:
        increases += 1
    four = three
    three = two
    two = one
f.close()
print("increases: {}".format(increases))
