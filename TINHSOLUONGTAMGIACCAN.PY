with open('TINHSOLUONGTAMGIACCAN.INP.txt', 'r') as fi:
    arr = list(map(int, fi.readline().split()))
with open('TINHSOLUONGTAMGIACCAN.OUT.txt', 'w') as fo:
    
    def dem_tam_giac(arr):
        n = len(arr)
        arr.sort()
        count = 0
        for i in range(n - 2):
            for j in range(i+1, n-1):
                k = j+1
                while k<n and arr[i]+arr[j]>arr[k]:
                    if arr[i]==arr[j] or arr[j]==arr[k] or arr[i] == arr[k]:
                        count+=1
                    k+=1
        return count
    b = dem_tam_giac(arr)
    fo.write(str(b))