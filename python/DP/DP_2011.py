MOD = 1000000 #문제 조건에 의해 나눌값

pwd = [0] + list(map(int, input())) # 편의를 위하여 0부터가 아닌 1부터 시작
n = len(pwd) -1 # 0을 추가하였으므로 -1 해줌
dp = [(0) for i in range(n+1)]
dp[0] = 1 #초기값 설정

for i in range(1, n+1):
	if pwd[i] != 0:
		dp[i] = dp[i-1]

	val = pwd[i-1]*10 + pwd[i]
	if 27 > val and val > 9:
		dp[i] += dp[i-2]
	dp[i] %= 1000000 #문제 조건에 의해 나누기

print(dp[n])
