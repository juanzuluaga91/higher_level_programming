#!/usr/bin/python3
for i in range(97, 123):
    xyzFascci = chr(i)
    nTxyz = "" + xyzFascci
    if i == 101 or i == 113:
        continue
    print("{}".format(nTxyz), end='')
