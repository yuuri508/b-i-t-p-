with open('DAYCON.INP.txt', 'r') as fi:
    s = list(map(int, fi.readline().split()))
    cong_sai = int(fi.readline())
with open('DAYCON.OUT.txt', 'w') as fo:
    ds = [s[0]]
    so_truoc = s[0]
    for i in range(1, len(s)):
        if s[i]-so_truoc == cong_sai:
            ds.append(s[i])
            so_truoc = s[i]  
    fo.write(f"{ds}\n")
    fo.write(f"{len(ds)}\n")


print(ds)
print(len(ds))