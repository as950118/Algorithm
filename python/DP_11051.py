import sys

n, k = map(int, sys.stdin.readline().split())
if n/2 > n-k:
    k = n-k
#n!/(k!(n-k)!)
ret = 0
def func():
    ret = 1
    b = 1
    c = 1
    for i in range(k):
        ret = ret * (n-i)
        if k-i>0:
            b = b * (k-i)
            if ret % b == 0:
                ret = ret // b
                b = 1
    if ret >=10007:
        ret = ret % 10007
    return ret

print(func())
