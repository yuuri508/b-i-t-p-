from math import sqrt
with open('TAMGIAC.INP', 'r') as fi:
    a, b, c = list(map(float, fi.readline().split()))
if a+b<c or a+c<b or c+b<a:
    xuat = 'khong phai 3 canh tam giac'
# pitago = c**2 = a**2+b**2 => c = sqrt(a**2+b**2)
else:
    if a==b==c:
        xuat = 'tam giac dieu'
    elif a==b:
        xuat = 'tam giac can'
    elif c**2 == a**2+b**2:
        xuat = 'tam giac vuong'
    else:
        xuat = 'tam giac thuong'
with open('TAMGIAC.OUT', 'w') as fo:
    fo.write(xuat)
