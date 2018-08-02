import sys
import math
from collections import deque

sys.setrecursionlimit(1000000000)

def func_1(i, j, k):
    if j==0:
        dp[i][j] = max(dp[i+k][j], dp[i+k][j+1]) + arr[i][j]

    elif j==1:
        dp[i][j] = max(max(dp[i+k][j], dp[i+k][j+1]), max(dp[i+k][j], dp[i+k][j-1])) + arr[i][j]

    elif j==2:
        dp[i][j] = max(dp[i+k][j], dp[i+k][j-1]) + arr[i][j]

def func_2(i,j,k):
    if j==0:
        dp_min[i][j] = min(dp_min[i+k][j], dp_min[i+k][j+1]) + arr[i][j]

    elif j==1:
        dp_min[i][j] = min(min(dp_min[i+k][j], dp_min[i+k][j+1]), min(dp_min[i+k][j], dp_min[i+k][j-1])) + arr[i][j]
    elif j==2:
        dp_min[i][j] = min(dp_min[i+k][j], dp_min[i+k][j-1]) + arr[i][j]
    
n = int(input())

arr = [[0]*(3) for i in range(2)]
dp = [[0]*(3) for i in range(2)]
dp_min = [[0]*(3) for i in range(2)]

arr[0] = list(map(int,input().split()))
for j in range(3):
    dp[0][j] = arr[0][j]
    dp_min[0][j] = arr[0][j]


for i in range(1, n):
    if i%2==0:
        arr[0] = list(map(int,input().split()))
        for j in range(3):
            func_1(0,j, 1)
            func_2(0,j,1)
    elif i%2==1:
        arr[1] = list(map(int,input().split()))
        for j in range(3):
            func_1(1,j, -1)
            func_2(1,j,-1)

if n%2==1:
    print(max(dp[0]), min(dp_min[0]))
else:
    print(max(dp[1]), min(dp_min[1]))
