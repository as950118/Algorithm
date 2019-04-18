import sys
INF = sys.maxsize
sys.setrecursionlimit(10**6)
a,b,c = [INF,3,2,1],[INF],[INF]

ret = INF
def func(a,b,c, val):
    if a==[INF] and (b==[INF] or c==[INF]):
        print(val)
        if ret>val:
            ret = val
        return 0
    for i in range(len(a)-1):
        temp = a.pop()
        if temp < b[-1]:
            func(a, b+[temp], c, val+1)
        if temp < a[-1]:
            func(a, b, c+[temp], val+1)
    a += [temp]
    for i in range(len(b)-1):
        temp = b.pop()
        if temp < a[-1]:
            func(a+[temp], b, c, val+1)
        if temp < c[-1]:
            func(a, b, c+[temp], val+1)
    b += [temp]
    for i in range(len(c)-1):
        temp = c.pop()
        if temp < a[-1]:
            func(a+[temp], b, c, val+1)
        if temp < b[-1]:
            func(a, b+[temp], c, val+1)
    c += [temp]
func(a,b,c,0)
print(ret)
