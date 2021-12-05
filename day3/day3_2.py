#!/usr/bin/env python

f = open('input.txt', 'r')
count = 0
up = 0
down = 0
forward = 0
litenliste, litenliste2 = [], []

def listen(_langliste, _posisjon, rating):
    _i, _j, _k = 0, 0, 0
    _t, _u = [], []
    for _rad in _langliste:
        chunks = list(_rad)
        _i += 1
        if chunks[_posisjon] == "0":
            _t.append(_rad)
            _j += 1
        if chunks[_posisjon] == "1":
            _u.append(_rad)
            _k += 1
    if rating == "oxygen":
        if _j > _k:
            return _t
        else:
            return _u
    if rating == "scrubber":
        if _k >= _j:
            return _t
        else:
            return _u
    else:
        print("feil!")


for line in f:
    line = line.replace('\n', '')  # remove '\n' only
    litenliste.append(line)
    litenliste2.append(line)
i = 0
while i < 12:
    litenliste = litenliste if len(litenliste) <= 1 else listen(litenliste, i, "oxygen")
    litenliste2 = litenliste2 if len(litenliste2) <= 1 else listen(litenliste2, i, "scrubber")
    i += 1
ox = int(litenliste[0], 2)
scb = int(litenliste2[0], 2)
print("ok, litenliste: {} = {}".format(litenliste, ox))
print("ok, litenliste2: {} = {}".format(litenliste2, scb))
print("multiplied: {}".format(ox * scb))



