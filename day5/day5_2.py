#!/usr/bin/env python

f = open('input.txt', 'r')
count = 0
a = [[0] * 1000 for i in range(1000)]

for line in f:
    line = line.replace('\n', '')  # remove '\n' only
    chunks = line.split("->")
    vektorV = list(map(int, chunks[0].split(",")))
    vektorH = list(map(int, chunks[1].split(",")))
    # linjer der x er konstant!
    if vektorV[0] == vektorH[0]:
        if vektorV[1] > vektorH[1]:
            i = vektorH[1]
            print("from x{} y{} to x{} y{} ".format(vektorV[0], i, vektorV[0], vektorV[1]))
            while i < vektorV[1] + 1:
                a[vektorV[0]][i] += 1
                i += 1
        if vektorV[1] < vektorH[1]:
            i = vektorV[1]
            print("from x{} y{} to x{} y{} ".format(vektorV[0], i, vektorV[0], vektorH[1]))
            while i < vektorH[1] + 1:
                a[vektorV[0]][i] += 1
                i += 1
    else:
        slope = int((vektorV[1] - vektorH[1]) / (vektorV[0] - vektorH[0]))
        intersect = int(vektorV[1] - slope * vektorV[0])
        print("slope {}".format(slope))

        if vektorV[0] > vektorH[0]:
            i = vektorH[0]
            print("from x{} y{} to x{} y{} ".format(i, vektorV[1], vektorV[0], vektorV[1]))
            while i < vektorV[0] + 1:
                a[i][slope * i + intersect] += 1
                i += 1
        if vektorV[0] < vektorH[0]:
            i = vektorV[0]
            print("from x{} y{} to x{} y{} ".format(i, vektorV[1], vektorH[0], vektorV[1]))
            while i < vektorH[0] + 1:
                a[i][slope * i + intersect] += 1
                i += 1
    count += 1

f.close()
overlapp = 0
i = 0
while i < 1000:
    j = 0
    print(''.join([str(int) for int in a[i]]))
    while j < 1000:
        if (a[i][j] > 1):
            overlapp += 1
        j += 1
    i += 1

print("antall overlapp: {} ".format(overlapp))
