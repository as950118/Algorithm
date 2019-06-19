n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
dp = [[-1 for i in range(n*100 +1)] for ii in range(n+1)]#0번째부터 idx번째까지 cur만큼의 값을 이용해서 만들 수 있는 최대 메모리
def func(idx, cur):
    if idx < 0:
        return 0
    if dp[idx][cur]!=-1:
        return dp[idx][cur]
    dp[idx][cur] = func(idx - 1, cur)
    if cur >= cost[idx]:
        dp[idx][cur] = max(dp[idx][cur], func(idx-1, cur-cost[idx]) + memory[idx])
    return dp[idx][cur]

def parametric():#이분탐색
    start = 0
    end = sum(cost)
    mid = 0
    while 1:
        if start>=end:
            return start
            break
        mid = (start+end) >> 1
        if func(n-1, mid) < m:
            start = mid+1
        else:
            end = mid

print(parametric())
