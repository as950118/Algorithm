import sys
sys.setrecursionlimit(10**6)
input = lambda:sys.stdin.readline().strip()

n, m = map(int, input().split())
dp = [[-1 for i in range(1<<14)] for ii in range(n*m)]

def func(cur, bit):
    if cur > n*m:
        return 0
    if cur == n*m:
        return bit==0

    if dp[cur][bit] != -1:
        return dp[cur][bit]

    if bit & 1: #만약 채워져있다면
        dp[cur][bit] = func(cur+1, (bit>>1)) #한칸을 미루고 진행
    else: #채워져있지 않다면
        dp[cur][bit] = func(cur+1, (bit>>1) | (1<<(m-1))) #한칸미룬 값과 맨 마지막을 or 연산함

        if cur%m != (m-1) and (bit & 1<<1) == 0: #그리고 마지막이 아니고
            dp[cur][bit] += func(cur+2, (bit>>2))
    return dp[cur][bit]
print(func(0,0)%9901)
