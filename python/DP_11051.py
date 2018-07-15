import sys

n, k = map(int, sys.stdin.readline().split())
if n/2 > n-k:
    k = n-k
#n!/(k!(n-k)!)
ret = 0
def func():
    ret = 1
    mod = 1
    for i in range(k):
        ret = ret * (n-i)
        if k-i>0:
            mod = mod * (k-i)
            if ret % mod == 0:
                ret = ret // mod
                mod = 1
    if ret >=10007:
        ret = ret % 10007
    return ret

print(func())
