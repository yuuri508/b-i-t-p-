with open('SODACBIET.INP.txt', 'r') as fi:
    n = list(map(int, fi.readline().split()))
with open('SODACBIET.OUT.txt', 'w') as fo:
    def so_dac_biet(n):
        ds = []
        tong = 0
        for i in range(1, n+1):
            if n%i==0:
                ds.append(i)
        tong = sum(ds)
        if tong>2*n:
            return True
        
    ds = []
    for i in n:
        if so_dac_biet(i):
            print(f"so {i} la so dac biet")
            ds.append(i)
            fo.write(f"so {i} la so dac biet\n")
        else:
            print(f"so {i} khong phai la so dac biet")
            fo.write(f"so {i} khong phai la so dac biet")
    print(len(ds))
    fo.write(str(len(ds)))