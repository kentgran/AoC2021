#!/usr/bin/env python

f = open('input.txt', 'r')
count = 0
chunks = []
result = []
instances = 0
storsum = 0

for line in f:
    line = line.replace('\n', '')

    kanvare = [[]] * 10
    chunks = line.split(' | ')
    chunks2 = " ".join(chunks)
    result = chunks2.split(' ')

    i = 0
    tmp = []
    vet1, vet7, vet4, vet8 = '', '', '', ''
    while i < len(result):
        sortert = sorted(result[i])

        if len(sortert) == 2:
            vet1 = sortert
        elif len(sortert) == 3:
            vet7 = sortert
        elif len(sortert) == 4:
            vet4 = sortert
        elif len(sortert) == 7:
            vet8 = sortert
        i += 1
    i = 0
    vetdiff = ''
    if len(vet4) > 0 and len(vet1) > 0:
        vetdiff = list(set(vet4) - set(vet1))

    vet0, vet2, vet3, vet5, vet6, vet9 = '', '', '', '', '', ''
    while i < len(result):
        sortert = sorted(result[i])
        if len(sortert) == 5:
            if len(vet1) > 0 and all(elem in sortert for elem in vet1):
                vet3 = sortert
            elif len(vetdiff) > 0 and all(elem in sortert for elem in vetdiff):
                vet5 = sortert
            elif len(vet1) > 0 and len(vetdiff) > 0:
                vet2 = sortert
            else:
                print("error5! {}".format(sortert))
        elif len(sortert) == 6:
            if len(vet4) > 0 and all(elem in sortert for elem in vet4):
                vet9 = sortert
            elif len(vetdiff) > 0 and all(elem in sortert for elem in vetdiff):
                vet6 = sortert
            elif len(vet4) > 0 and len(vetdiff) > 0:
                vet0 = sortert
            else:
                print("error6! {}".format(sortert))
        i += 1
    print("{}: 0:{} 1:{} 2:{} 3:{} 4:{} 5:{} 6:{} 7:{} 8:{} 9:{}".format(count, vet0, vet1, vet2, vet3, vet4, vet5,
                                                                         vet6, vet7, vet8, vet9))
    i = 0
    j = ''
    result = chunks[1].split(' ')
    while i < len(result):
        sortert = sorted(result[i])
        if sortert == vet1:
            j += '1'
        elif sortert == vet2:
            j += '2'
        elif sortert == vet3:
            j += '3'
        elif sortert == vet4:
            j += '4'
        elif sortert == vet5:
            j += '5'
        elif sortert == vet6:
            j += '6'
        elif sortert == vet7:
            j += '7'
        elif sortert == vet8:
            j += '8'
        elif sortert == vet9:
            j += '9'
        elif sortert == vet0:
            j += '0'
        else:
            print("error!")
        i+=1
    print("{}".format(j))
    storsum += int(j)
    count += 1
print("totalt: {}".format(storsum))
