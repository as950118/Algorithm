import sys

N,M,K = map(int, sys.stdin.readline().split())


dp = [[(-1) for i in range(M+1)] for ii in range(N+1)]

def getDP(n, m):
    if n==0 or m==0:
        return 1
    if dp[n][m] != -1:
        return dp[n][m]

    dp[n][m] = getDP(n-1, m) + getDP(n, m-1)
    return dp[n][m]

def func(n, m, k):
    ret = ""
    if n==0:
        ret += 'z'*m
        return ret
    if m==0:
        ret += 'a'*n
        return ret

    if getDP(n-1, m) > k:
        ret += 'a'
        ret += func(n-1,m,k)
        return ret
    else:
        ret += 'z'
        ret += func(n, m-1, k-getDP(n-1, m))
        return ret

if K > getDP(N, M):
    print(-1)
else:
    print(func(N,M,K-1))
