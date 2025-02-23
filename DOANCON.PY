def so_nho_nhat(arr, s):
    n = len(arr)
    min_sub = float('inf')
    start = 0
    c_sum = 0
    
    for end in range(n):
        c_sum += arr[end]
        
        while c_sum <= s:
            min_sub = min(min_sub, end - start + 1)
            c_sum -= arr[start]
            start +=1
    return min_sub if min_sub != (float('inf')) else 0