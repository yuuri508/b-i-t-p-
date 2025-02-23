def so_nguyen_to(n):
    
    if n<2:
        return False
    else:
        for i in range(2, (n//2)+1):
            if n%i!=0:
                return True
            
    return False
n = int(input('nhap so luong so nguyen to mon muon: '))
k= []
d= 0
for i in range(1, n+1):
    i = int(input(f"nhap so n{i}: "))
    k.append(i)
for i in k:
    if so_nguyen_to(i):
        d+=1
print(d)