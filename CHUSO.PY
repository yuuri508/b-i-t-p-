with open('CHUSO.INP.txt', 'r') as fo:
    n = int(fo.readline())
with open('CHUSO.OUT.txt', 'w') as fi:
    n = [int(i) for i in str(n)]
    print(n)
    dem = len(n)
    fi.write(f"so luong cac chu so{n} la: {dem}")