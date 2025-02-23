n = [1,2,3] 
tong = 0 
for i in range(len(n)): 
    for j in range(i, len(n)): 
        tong += sum(n[i:j+1]) 
print(tong)