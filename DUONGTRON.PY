from math import sqrt
with open ('DUONGTRON.INP', 'r') as fo:
    ban_kinh, xa, ya, xo, yo = list(map(float, fo.readline().split()))
#sqrt(xa-xb)^2+(ya-yb)^2
d = sqrt((xa-xo)**2+(ya-yo)**2)
if d < ban_kinh:
    a = 'diem a nam trong duong tron'
elif d==ban_kinh:
    a = 'diem a nam tren duong tron'
else:
    a = 'diem a nam ngoai duong tron'
print(a)
with open ('DUONGTRON.OUT', 'w') as fi:
    fi.write(a) 