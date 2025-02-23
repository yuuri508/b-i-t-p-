from math import sqrt
xa, ya= list(map(int, input('nhap toa do xa, ya: ').split()))
xb, yb = list(map(int, input('nhap toa do xb, yb: ').split()))
xc, yc = list(map(int, input('nhap toa do xc, yc: ').split()))
print(f"2{xa}-{ya}+1=0")
print(f"2{xb}-{yb}+1=0")
ab = sqrt((xa-xb)**2+(ya-yb)**2)
ac = sqrt((xa-xc)**2+(ya-yc)**2)
bc = sqrt((xc-xb)**2+(yc-yb)**2)
if ab+ac>bc and ab+bc>ac and bc+ac>ab:
    c = ab+ac+bc
    p = c/2
    s = sqrt(p*(p-ab)*(p-ac)*(p-bc))
    print(f"dien tich tam giac la: {s}")
else:
    print('khong phai la 2 canh tam giac')
