import sys
sys.setrecursionlimit(1000000000)

dp = [0]*1000000
ret = 0
mod = 1000000000

def func(n, i, k):#횟수 위치 (계단수) 현재값
    global ret
    if n<=i:
        ret = ret+1
        if ret==mod:
            ret = 0
        return 0
    if k<1 or k>8:
        if k<9:
            func(n, i+1, k+1)
        elif k>0:
            func(n, i+1, k-1)
        else:
            return 0
    else:
        func(n, i+1, k+1)
        func(n, i+1, k-1)



N = int(input())
for k in range(1, 10):
    func(N, 1, k)
print(ret)
