'''
frcfcrf
'''
rotation = ['f','r','c','f','c','r','f']
f,r,c = map(int, input().split())
min_frc = min(f*2,r*3,c*3)
if min_frc == f*2:
    ret = 7*(f//3)
    r -= 2*(f//3)
    c -= 2*(f//3)
    f -= 3*(f//3)
elif min_frc == r*3:
    ret = 7*(r//2)
    f -= 3*(r//2)
    c -= 2*(r//2)
    r -= 2*(r//2)
elif min_frc == c*3:
    ret = 7*(c//2)
    f -= 3*(c//2)
    r -= 2*(c//2)
    c -= 2*(c//2)
list_ret = []
for k in range(7):
    tf = f
    tr = r
    tc = c
    tret = ret
    for j in range(k,7):
        if rotation[j] == 'f':
            if not tf:
                break
            tf -= 1
            tret += 1
        elif rotation[j] == 'r':
            if not tr:
                break
            tr -= 1
            tret += 1
        elif rotation[j] == 'c':
            if not tc:
                break
            tc -= 1
            tret += 1
    for j in range(7):
        if rotation[j] == 'f':
            if not tf:
                break
            tf -= 1
            tret += 1
        elif rotation[j] == 'r':
            if not tr:
                break
            tr -= 1
            tret += 1
        elif rotation[j] == 'c':
            if not tc:
                break
            tc -= 1
            tret += 1
    list_ret.append(tret)
print(max(list_ret))
