from math import gcd
n =int(input('nhap so luong so mong muon: '))
ds = []
for i in range(1, n+1):
    a = int(input(f"nhap so n{i}: "))
    ds.append(a)
def so_nguyen_to(n):
    if n<2:
        return False
    else:
        for i in range(2, (n//2)+1):
            if n % i!=0:
                return True
    return False
ds_nguyen_to = []
for i in ds:
    if so_nguyen_to(i):
        ds_nguyen_to.append(i)
uoc_chung = 0
a0 = ds[0]
a1 = ds[1]
for i in range(2, len(ds)):
    uoc_chung = gcd(a0, a1)
    a0 = a1
    a1 = ds[i]
print(ds_nguyen_to)
print(uoc_chung)
print(sorted(ds))