import sys
sys.setrecursionlimit(10**8)
n, k = map(int, input().split())
arr = list(map(int, input().split()))
ret = sys.maxsize
def func(idx, remain):
    global ret
    if n-idx<2*remain:
        return 0
    if n-idx==2*remain:
        return sum(arr[idx+1::2]) - sum(arr[idx::2])
    for i in range(idx,n):
        ret = min(ret, arr[i]-arr[idx]+func(i, remain-1))
    return ret
print(func(0,k))
