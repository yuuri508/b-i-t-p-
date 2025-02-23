fi = open('CAU1.INP')
o = list(fi.readline().split())
o = [int(i) for i in o]
def so_nguyen_to(n):
    if n<2:
        return False
    else:
        for i in range(2, (n//2)+1):
            if n%i==0:
                return False
    return True
ab = []
cd = []
for i in range(o[0], o[1]):
    if so_nguyen_to(i):
        ab.append(i)
for i in range(o[2], o[3]):
    if so_nguyen_to(i):
        ab.append(i)
if len(ab)>len(cd):
    print('an la nguoi thang')
elif len(ab)<len(cd):
    print('binh la nguoi thang')
else:
    print('ca 2 hue nhau')