k = [6, 3]
a = [3, 2, 4, 6, 3, 7]
tong_k = sum(k)
a0 = a[0]
a1 = a[1]
tong = 0
tong1 = 0
ds = []
if sum(a)%tong_k == 0:
    print(f"day dai nhat co tong chia het cho k gom {len(a)} la {a}")
else:
    for i in range(len(a)):
        tong = a0+a1
        if tong%tong_k == 0:
            