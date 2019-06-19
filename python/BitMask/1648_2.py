import sys
sys.setrecursionlimit(10**6)
input = lambda:sys.stdin.readline().strip()

n, m = map(int, input().split())
dp = [[[-1 for i in range(1<<14)] for ii in range(m)] for iii in range(n)]
'''
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
'''
def func(x,y, bit):
    if x>m-1 or y>n-1:
        return 0
    if x==m-1 and y==n-1:
        return bit==0

    if dp[y][x][bit] != -1:
        return dp[y][x][bit]

    if bit & 1:
        if x==m-1:
            dp[y][x][bit] = func(0, y+1, (bit>>1))
        else:
            dp[y][x][bit] = func(x+1, y, (bit>>1))
    else:
        if x==m-1:
            dp[y][x][bit] = func(0, y+1, (bit>>1) | (1<<(m-1)))
        else:
            dp[y][x][bit] = func(x+1, y, (bit>>1) | (1<<(m-1)))
            if bit & 1<<1 == 0:
                if x == m-2:
                    dp[y][x][bit] += func(0, y+1, (bit>>2))
                else:
                    dp[y][x][bit] += func(x+2, y, (bit>>2))
    return dp[y][x][bit]
print(func(0,0,0)%9901)
