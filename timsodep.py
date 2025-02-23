n = int(input('nhap so luong phan tu a: '))
a = []
for i in range(1, n+1):
    i = int(input(f"nhap so n{i} muon them vao danh sach: "))
    a.append(i)
tong = sum(a)
if tong%len(a)==0:
    print(f"tong so pha tu trong danh sach {a} la: {tong} la so dep")
else:
    print(f"tong so pha tu trong danh sach {a} la: {tong} khong phai la so dep")
chuoi = []
ds_so_dep = []
for i in a:
    chuoi = [int(j) for j in str(i)]
    if int(sum(chuoi))%len(chuoi)==0:
        ds_so_dep.append(i)
vi_tri = []
print(ds_so_dep)
for i in range(len(a)):
    d = a[i]
    for j in ds_so_dep:
        if j==d:
            vi_tri.append(i+1)
print(vi_tri)