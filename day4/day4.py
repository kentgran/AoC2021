#!/usr/bin/env python

f = open('input.txt', 'r')
count = 0


class Brett:

    def __init__(self):
        self.matrix = []
        self.flagtrix = []

    def addRow(self, rad):
        chunks = int(rad[0:2]), int(rad[3:5]), int(rad[6:8]), int(rad[9:11]), int(rad[12:14])
        self.matrix.append(chunks)
        self.flagtrix.append([0, 0, 0, 0, 0])
        return True

    def getRow(self, radnummer):
        return self.matrix[radnummer]

    def getColumn(self, kolonnenummer):
        kolonne = []
        for rad in self.matrix:
            kolonne.append(rad[kolonnenummer])
        return kolonne

    def matchRow(self, radnummer, serie):
        return set(self.getRow(radnummer)) & set(serie)

    def matchColumn(self, kolonnenummer, serie):
        return set(self.getColumn(kolonnenummer)) & set(serie)

    def setFlagTrix(self, trukket):
        i = 0
        while i < 5:
            j = 0
            while j < 5:
                if self.matrix[i][j] == trukket:
                    self.flagtrix[i][j] = 1
                j += 1
            i += 1
        return 1

    def sjekkBingoRad(self, rad):
        return sum(self.flagtrix[rad])

    def sjekkBingoKolonne(self, kolonnenummer):
        kolonne = []
        for rad in self.flagtrix:
            kolonne.append(rad[kolonnenummer])
        return sum(kolonne)

    def sumUnmarked(self):
        summerer = 0
        i = 0
        while i < 5:
            j = 0
            while j < 5:
                summerer += self.matrix[i][j] if self.flagtrix[i][j] == 0 else 0
                j += 1
            i += 1
        return summerer


testbrett = [Brett] * 100
flagg = False
brettCount = 0

for line in f:
    line = line.replace('\n', '')
    if count == 0:
        bingoserie = list(map(int, line.split(',')))
    elif line == "":
        if flagg:
            brettCount += 1
        # gjør klar et nytt brett
        testbrett[brettCount] = Brett()
        flagg = True
    else:
        testbrett[brettCount].addRow(line)
    count += 1
f.close()

l = 0
while l < len(bingoserie):
    k = 0
    talletEr = bingoserie[l]
    while k < len(testbrett):
        testbrett[k].setFlagTrix(talletEr)
        k += 1
    if l > 4:
        # sjekk om vi har fått bingo
        m = 0
        while m < len(testbrett):
            n = 0
            while n < 5:
                o = testbrett[m].sjekkBingoRad(n)
                if o > 4:
                    print("bingo!: brett: {} rad: {} ".format(m, n))
                    n = 5
                    m = len(testbrett)
                    l = len(bingoserie)
                o = testbrett[m].sjekkBingoKolonne(n)
                if o > 4:
                    unmarked = testbrett[m].sumUnmarked()
                    print("bingo!: brett: {} kolonne: {} ".format(m, n))
                    print("brett: {}".format(testbrett[m].matrix))
                    print("flagg: {}".format(testbrett[m].flagtrix))
                    print("sum unmarked: {}".format(unmarked))
                    print("tot: {}".format((talletEr * unmarked)))
                    n = 5
                    m = len(testbrett)
                    l = len(bingoserie)
                n += 1
            m += 1
    l += 1
