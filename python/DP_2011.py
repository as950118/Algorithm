import sys
sys.setrecursionlimit(1000000)
from collection import deque

n = sys.stdin.readline()
arr = deque()
for i in n:
	arr.append(i)
l = len(arr)
dp = [0]*(l)
ret = 0

def func(i):
	if dp[i] != 0:
		return dp[i]
	dp[i] = 1
	if i+1<l:
		if arr[i+1]==0:
			return dp[i]
			if arr[i]==2:
				if arr[i+1]<7:
					temp = 2
					if func(i+1) == 1:
						temp = 3
					else:
						k
			elif arr[i]==1:

	else:

		
