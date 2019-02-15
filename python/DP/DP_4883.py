import sys
sys.setrecursionlimit(10000000)
def func(y,x):
	if y == n:
		if x==1:
			return arr[y][x] + arr[y][x+1]
		elif x==2:
			return arr[y][x]
		else:
			return 100000000
	if dp[y][x] != -1:
		return dp[y][x]
	if x == 1:
		dp[y][x] = min(func(y+1,x), func(y+1,x+1), func(y,x+1))
	elif x == 2:
		dp[y][x] = min(func(y+1,x-1), func(y+1,x), func(y+1,x+1), func(y,x+1))
	else:
		dp[y][x] = min(func(y+1,x-1), func(y+1,x))
	dp[y][x] += arr[y][x]
	return dp[y][x]
t = 0
while 1:
	t+=1
	n = int(sys.stdin.readline())
	if n == 0:
		break
	arr = [[0,0,0,0]]
	dp = [[(-1) for i in range(4)] for ii in range(n+1)]
	for i in range(n):
		arr.append([0] + list(map(int, sys.stdin.readline().split())))
	print(str(t)+". "+ str(func(1,2)))
