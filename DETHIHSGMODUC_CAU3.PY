s = 'Quang ngai que huong'
dem1 = 0
dem2 = 0
chu1 = []
chu2 = []
for i in s:
    if i.isalpha():
        dem1+=1
        chu1.append(i)
    
    else:
        if len(chu1)>len(chu2):
            dem2 = dem1
            chu2 = chu1[:]
            dem1 = 0
        chu1 = []
if len(chu1)>len(chu2):
    chu2 = chu1[:]
chu2 = " ".join(chu2)
print(chu2)