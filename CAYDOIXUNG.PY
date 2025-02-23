with open('CAYDOIXUNG.INP.txt', 'r') as fi:
    k = list(map(int, fi.readline().split()))
    n = list(map(int, fi.readline().split()))
with open('CAYDOIXUNG.OUT.txt', 'w') as fo:
    chenh_lech = max(k) - min(k)
    print(chenh_lech)
    n.sort()
    dao_nguoc = []
    n = [i for i in n[:: -1]]
    print(n)
    tong = 0
    a = max(n)
    for i in range(1, len(n)):
        lon_nhat = a
        for j in range(i, len(n)):
            if 0<=lon_nhat - n[j]<=chenh_lech:
                tong+=1
            a = n[i]
        
        
    fo.write(f"{tong}")