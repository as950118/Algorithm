import sys
inf = sys.maxsize
n,k = map(int, input().split())
'''
ret = 0
def func(idx, cur, count, next):
    global ret
    if idx==n:
        if cur==k:
            return count
        else:
            return 0
    if idx==n-1 and cur==1:
        return count+1
    if cur>1:
        ret = max(ret, func(idx+1, cur-1, count+1, next), func(idx+1, cur+next, count, next+1))
    else:
        ret = max(ret, func(idx+1, cur+next, count, next+1))
    return ret
print(func(0,0,0,1))
'''
for i in range(1, n+1):
    temp = (i)*(i+1)//2
    if temp - (n-i) == k:
        print(n-i)
        break
