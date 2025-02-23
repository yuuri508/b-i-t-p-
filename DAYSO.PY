with open('DAYSO.INP.txt', 'r') as fi:
    a = list(map(int, fi.readline().split()))
with open('DAYSO.OUT.txt', 'w') as fo:
    def so_nguyen_to(n):
        if n<2:
            return False
        else:
            for i in range(2, (n//2)+1):
                if n%i!=0:
                    return True
        return False
    tang_dan = sorted(a)
    so_chan = []
    nguyen_to = []
    for i in a:
        if i%2==0:
            so_chan.append(i)
        if so_nguyen_to(i):
            nguyen_to.append(i)
    tong = sum(so_chan)
    fo.write(f"{tang_dan}\n")
    fo.write(f"{so_chan}\n")
    fo.write(f"{nguyen_to}\n")