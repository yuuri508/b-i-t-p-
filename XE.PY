with open ('XE.INP', 'r') as fi:
    xe = list(map(int, fi.readline()))
print(xe)
with open('KHOI_LUONG_XE.INP', 'r') as kl:
    khoi_luong = list(map(int, kl.readline().split()))
print(khoi_luong)
tong_khoi_luong = sum(khoi_luong)
tong_khoi_luong = str(tong_khoi_luong)
print(tong_khoi_luong)

with open ('CAN.OUT', 'w') as fo:
    fo.write(tong_khoi_luong)

vi_pham = []
for i in range(len(khoi_luong)):
    if khoi_luong[i]>20:
        vi_pham.append(i+1)
vi_pham = str(vi_pham)

with open('XE.OUT', 'w') as ho:
    ho.write(vi_pham)