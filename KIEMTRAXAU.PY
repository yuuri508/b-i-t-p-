s = 'abc123bba567ajsj5078kkf099999'
t = [i for i in str(s)]
dem = 0
so1 = []
so2 = []
for i in t:
    if i.isdigit():
        so1.append(i)
    else:
        for j in so1:
            if j==0:
                so1.remove(j)
            else:
                break
        if len(so1)>=len(so2):
            so2 = so1[:]
            so1 = []
        
for i in so1:
    if i==0:
        so1.remove(i)
    else:
        break       
if len(so1)>=len(so2):
        so2 = so1[:]
        so1 = [] 
print(so2)
print(so1)
