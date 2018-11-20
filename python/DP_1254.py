import sys

s = input()
n = len(s)

dp = [[(-1) for i in range(n)] for ii in range(n)]
def main():
    def func(start, end):
        if start>=end:
            return 1
        if dp[start][end] != -1:
            return dp[start][end]
        if s[start] != s[end]:
            return 0
        dp[start][end] = func(start+1, end-1)
        return dp[start][end]
    for i in range(n):
        if func(i, n-1) != 0:
            return n+i

print(main())
