def cat_list(a):
    return (len(a)//2)+1
a = [1,2,3,3,2,2,1,1,1,3,1]
dem0 = 0
dem1 = 0
a0 = a[0]
a1 = a[1]
ls = []
ls1 = []
ls.append(a0)
ls.append(a1)
for i in range(2, len(a)):
    if a[i] in ls:
        dem0 +=1
        ls.append(a[i])
    else:
        if len(ls)>len(ls1):
            ls1 = ls[:]
        ls = []
        a0 = a1
        a1 = a[i]
        ls.append(a0)
        ls.append(a1)
if len(ls)>len(ls1):
    ls1 = ls[:]
print(len(ls1))
print(ls1)

