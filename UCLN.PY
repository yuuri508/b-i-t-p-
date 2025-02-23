from math import gcd
with open('UCLN.INP.txt', 'r') as fi:
    s = list(map(int, fi.readline().split()))
with open('UCLN.OUT.txt', 'w') as fo:
    s1 = s[0]
    s2 = s[1]
    ucln = gcd(s1, s2)
    for i in range(2, len(s)):
        s1 = s[i]
        ucln = gcd(ucln, s1)
    fo.write(f"uoc chung lon nhat cua day la: {ucln}")
print(ucln)