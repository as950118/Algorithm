import math

n = int(input())
dp = [[-1 for i in range(10)] for i in range(10**6)]
val = [0 for i in range(10)]
for j in range(1, n+1):
    cur_n = j
    ln = int(math.log10(cur_n)) #로그값을 이용해 자릿수 구하기
    for i in range(1,ln+2):
        try:
            if max(dp[cur_n]) != -1:
                for j in range(10):
                    if dp[cur_n][j] != -1:
                        val[j] += dp[cur_n][j]
                break

            dp[cur_n] = [0 for j in range(10)]
            dp[cur_n][cur_n%(10**i)] += 1
        except:
            pass
        val[cur_n%(10**i)] += 1
        cur_n = cur_n//(10**(i))

for i in val:
    print(i, end=" ")
