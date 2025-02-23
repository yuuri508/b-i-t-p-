from math import sqrt
with open('TIMKHOANCACHSANHAT.INP', 'r') as fo:
    toa_do = list(map(int, fo.readline().split()))
with open('TIMKHOANCACHSANHAT.OUT', 'w') as fi:
    xo = 0
    yo = 0
    toa_do = [int(i) for i in toa_do]
    diem_max = 0
    khoang_cach_max = 0
    for i in range(len(toa_do)):
        x = toa_do[i]