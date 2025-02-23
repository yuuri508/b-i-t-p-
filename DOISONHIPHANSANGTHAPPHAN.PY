n = 100000
tong = 0
n = [int(i)for i in str(n)]
print(n)
dem = len(n)-1
for i in n:
    tong += i*2**dem
    dem -=1
print(tong)