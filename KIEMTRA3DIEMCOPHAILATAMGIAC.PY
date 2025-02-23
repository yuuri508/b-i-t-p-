from math import sqrt
with open ('KIEMTRA3DIEMCOPHAILATAMGIAC.INP', 'r') as fi:
    xa, ya, xb, yb, xc, yc = list(map(int, fi.readline().split()))

def kiem_tra_3_diem(xa, ya, xb, yb, xc, yc):
    ket_qua = xa*(yb-yc)+xb*(yc-ya)+xc*(ya-yb)
    if ket_qua != 0:
        return True
    else:
        return False
if kiem_tra_3_diem(xa, ya, xb, yb, xc, yc):
    a = yb-ya
    b = xa-xb
    c = xb*ya - xa*yb
    print(f"{a}x+{b}y+{c} = 0")
    ab = sqrt((xa-xb)**2+(ya-yb)**2)
    ac = sqrt((xa-xc)**2+(ya-yc)**2)
    cb = sqrt((xc-xb)**2+(yc-yb)**2)
    ab = round(ab, 0)
    ac = round(ac, 0)
    cb = round(cb, 0)
    print(ab, ac, cb)
    if ab+cb>ac and ac+ab>cb and cb+ac>ab:
        c1 = ac+cb+ab
        p = c1/2
        s = sqrt(p*(p-ac)*(p-cb)*(p-ab))
        with open('KIEMTRA3DIEMCOPHAILATAMGIAC.out', 'w') as fo:
            fo.write(f"{a}x+{b}y+{c} = 0\n")
            fo.write(f"dien tich tam giac a, b, c la: {s}")
    else:
        print('khong phai la tam giac')
        with open('KIEMTRA3DIEMCOPHAILATAMGIAC.out', 'w') as fo:
            fo.write(f"{a}x+{b}y+{c} = 0\n")
            fo.write(f"khong phai la tam giac!")
    