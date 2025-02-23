n = int(input('nhap so lan muon binh phuong: '))
x = int(input('nhap so mong muon: '))
ds = []
for i in range(n):
    ds.append(x)
    tong = sum(int(i)**2 for i in str(x))
    x = tong
print(*ds)