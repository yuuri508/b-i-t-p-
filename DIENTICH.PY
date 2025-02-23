with open('DIENTICH.INP.txt', 'r') as fi:
    a = float(fi.readline())
with open('DIENTICH.OUT.txt', 'w') as fo:
    s_vuong = a*a
    pi = 3.14
    s_tron = (a/2)**2*pi
    s_cheo = s_vuong - s_tron
    s_cheo = str(round(s_cheo, 2))
    fo.write(s_cheo)