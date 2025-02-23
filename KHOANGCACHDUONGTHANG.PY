from math import sqrt
with open('KHOANGCACHDUONGTHANG.INP', 'r') as fi:
    xa, ya, xb, yb, xc, yc = list(map(int, fi.readline().split()))

with open('KHOANGCACHDUONGTHANG.out', 'w') as fo:
    def kiem_tra_3_diem(xa, ya, xb, yb, xc, yc):
        ket_qua = xa*(yb-yc)+xb*(yc-ya)+xc*(ya-yb)
        if ket_qua != 0:
            return True
        else:
            return False

    a = yb-ya
    b = xa-xb
    c = xb*ya - xa*yb
    fo.write(f"{a}x+{b}y+{c} = 0\n")
    
    if kiem_tra_3_diem(xa, ya, xb, yb, xc, yc):
        ab = sqrt((xa-xb)**2+(ya-yb)**2)
        ac = sqrt((xa-xc)**2+(ya-yc)**2)
        cb = sqrt((xc-xb)**2+(yc-yb)**2)
        if ab+ac>cb and ab+xb>ac and ac+cb>ab:
            c = ab+ac+cb
            p = c/2
            s = sqrt(p*(p-ac)*(p-ab)*(p-cb))
            s = round(s, 0)
            fo.write(f"tam giac a, b, c co dien tich la: {s}\n")
            if ab==ac:
                fo.write('tam giac a, b, c la tam giac can')
            else:
                fo.write('tam giac a, b, c khong phai la tam giac can')
    