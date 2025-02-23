def so_chinh_phuong(n):
    a = []
    for i in range(1, n):
        if n==i**2:
            a.append(i)
    return a
def so_nguyen_to(n):
    if n<2:
        return False
    else:
        for i in range(2, (n//2)+1):
            if n%i!=0:
                return True
    return False
n = list(map(int, input('nhap n: ').split()))
a = []
k = []
for i in n:
    for j in range(1, i+1):
        if i%j==0:
            a.append(j)
if len(a)>3:
    print(f"{n} la hop so")
    for i in n:
        if so_chinh_phuong(i):
            print(f"{i} cung la so chinh phuong")
    for i in n:
        if so_nguyen_to(i):
            k.append(i)
    print(f"{k} la so nguyen to")
elif len(a)<3:
    print(f"{n} khong phai la hop so")
    for i in a:
        if so_chinh_phuong(i):
            print(f"{i} cung la so chinh phuong")
    for i in n:
        if so_nguyen_to(i):
            k.append(i)
    print(f"{k} la so nguyen to")

