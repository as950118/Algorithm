s, e = map(int, input().split())
if s>e:
    s,e = e,s

for j in range(1,10):
    for i in range(s,e+1):
        print('%d'%i, '*', '%d'%j, '=', '%2d'%(i*j), end="   ")
    print("")
