import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
n,k = map(int, input().split())
dp = [defaultdict(lambda:-1) for sol in range(k+1)]
def func(cur,val,arr,Sum):
    if cur>k or Sum>n:
        return 0
    if cur==k and Sum==n:
        return arr
    if dp[cur][Sum]!=-1:
        return dp[cur][Sum]
    dp[cur][Sum] = 0
    for i in range(1, val+1):
        if i+val>n:
            break
        dp[cur][Sum] = func(cur+1, val+i, arr+[val+i], Sum+val+i)
        if dp[cur][Sum]:
            break
    return dp[cur][Sum]
for i in range(1,n+1):
    ret = func(1,i,[i],i)
    if ret:
        break
if ret:
    print("YES")
    for i in ret:
        print(i, end=" ")
else:
    print("NO")
