import sys
sys.setrecursionlimit(10**6)
input = lambda:sys.stdin.readline().strip()

bit_list = [0, (1<<0), (1<<1 + 1<<0), (1<<2), (1<<2 + 1<<1)] #000, 001, 011, 100, 110

def next_bit(bit):
    ret = []
    for i in range(m):
        if bit ^ (1<<i): #0일 경우

            if i != m-1: #그리고 마지막이 아닐경우



def func(cur, bit):
    if cur<0:
        return 0
    if cur==0:
        return bit==0
    if dp[cur][bit] != -1:
        return dp[cur][bit]

    return dp[cur][bit]

n, m = map(int, input().split())
if n<m: #n을 더 크수로
    n,m = m,n
dp = [[-1 for i in range(1<<m)] for ii in range(n)]
