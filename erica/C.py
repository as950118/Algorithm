import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[(0) for i in range(2)] for ii in range(m+1)]
dp = [(-1) for i in range(m+1)]

for i in range(1,m+1):
    arr[i][0], arr[i][1] = map(int, sys.stdin.readline().split())

def func(cur, idx):
    if idx > n:
        return 0
    if idx == n:
        return arr[idx][1]
    try:
        chk.index(-1)
    except:
        print("sex")
        return arr[idx][1]
    if dp[idx] != -1:
        return dp[idx]
    dp[idx] = 0
    chk[idx] = 0

    for i in range(idx, m+1):
        dp[idx] = max(dp[idx], func(idx+arr[i][0]))
    dp[idx] += arr[idx][1]
    return dp[idx]

for i in range(1, m+1):
    chk = [(-1) for j in range(m+1)]
    func(i, i-1)
    print(dp)
