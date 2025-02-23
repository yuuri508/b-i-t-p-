import itertools
def giong_nhau(n):
    return len(set(n))==1
n = ['a', 'a', 'a']
if giong_nhau(n):
    print(f"{n}")
else:
    ds = list(itertools.permutations(n))
    print(ds, len(ds))