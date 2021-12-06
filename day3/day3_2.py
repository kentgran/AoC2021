#!/usr/bin/env python

f = open('input.txt', 'r')
up, down, forward = 0, 0, 0
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
    line = line.replace('\n', '')
    litenliste.append(line)
    litenliste2.append(line)
i = 0
while i < 12:
    litenliste = litenliste if len(litenliste) <= 1 else listen(litenliste, i, "oxygen")
    litenliste2 = litenliste2 if len(litenliste2) <= 1 else listen(litenliste2, i, "scrubber")
    i += 1
ox = int(litenliste[0], 2)
scb = int(litenliste2[0], 2)
print("multiplied: {}".format(ox * scb))



