with open('KIEMTRADOIXUNG.INP.txt', 'r') as fo:
    s = list(map(str, fo.readline()))
with open('KIEMTRADOIXUNG.OUT.txt', 'w')as fi:
    def palindom(s):
        if s==s[:: -1]:
            return True
        return False
    if palindom(s):
        print('true')
        fi.write(f"True")
    else:
        print('false')
        fi.write(f"False")