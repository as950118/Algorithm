import sys
import math
from collections import deque
sys.setrecursionlimit(1000000000)

n = int(sys.stdin.readline())
arr = deque(map(int, sys.stdin.readline().split()))
dp = [[-1]*(n) for i in range(n)]


def func(start, end):
	if start>=end:
		return 1
	if dp[start][end] != -1:
		return dp[start][end]
	if arr[start] != arr[end]:
		return 0
	dp[start][end] = func(start+1, end-1)
	return dp[start][end]


for i in range(int(sys.stdin.readline())):
	temp = list(map(int,sys.stdin.readline().split()))
	print(func(temp[0]-1, temp[1]-1))
