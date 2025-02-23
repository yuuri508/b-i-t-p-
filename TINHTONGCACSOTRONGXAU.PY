s = "abcd123aad22a05" 
so = []
tong = 0
s = [i for i in str(s)]
for i in s:
    if i.isdigit():
        if i==0:
            continue
        else:
            so.append(i)
so = [int(i) for i in so]
so1 = []
for i in range(len(so1)):
    a = str(i)
    for j in s:
        if a==j:
            so1.append(i)
        else:
            p = ''.join(map(str, so1))
            p = int(p)
            print(p)
            tong+=p
            so1 = []
        
        
