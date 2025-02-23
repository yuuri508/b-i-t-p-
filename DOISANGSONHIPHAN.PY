n = 3232
ds = []
if n<0:
    print('khong hop le')
else:
    while n/2 !=0:
        tp = n%2
        ds.append(tp)
        g = n//2
        n = g
    nguoc = []
    for i in ds[:: -1]:
        nguoc.append(i)
    nguoc = "".join(map(str, nguoc))
    print(nguoc)