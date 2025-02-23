def duong_thang_di_qua_2_diem(xa, ya, xb, yb):
    a = yb-ya
    b = xa-xb
    c = -(a*xa+b*ya)
    print(f"{a}x+{b}y+{c}=0")
    return a, b, c
xa, ya, xb, yb, xc, yc = list(map(int, input('nhap cac toa do x,y cua abc: ').split()))
print(duong_thang_di_qua_2_diem(xa, ya, xb, yb))

