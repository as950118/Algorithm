'''
1 = 1 = 1
2 = 1 1 / 2 = 2
3 = 1 1 1 / 2 1 / 1 2 / 3 = 4

4 = 3 1 => 7
5 = 4 1 => 13

6 = => 24
7 = 3 2 2 / 2 3 2 / 2 2 3 => 44

8 = 81
9 = 149
10 = 274
11 = 504
4 = 1 1 1 1 / 2 1 1 / 1 2 1 / 1 1 2 / 2 2 / 3 1 / 1 3 = 7
5 = 1 1 1 1 1 / 2 1 1 1 / 1 2 1 1 / 1 1 2 1 / 1 1 1 2 / 2 2 1 / 2 1 2 / 1 2 2 / 3 1 1 / 1 3 1 / 1 1 3 / 3 2 / 2 3 = 13
6 = 5 1 / 1 5 => 25
7 = 6 1 / 1 6 => 49
'''

T = int(input())

dp = [0]*12
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

answer = [0]*12

def func(n, i):
    if n<i:
        return 0
    if dp[i]!=0:
        pass
    else:
        dp[i]+=dp[i-1]+dp[i-2]+dp[i-3]
    func(n, i+1)

for i in range(0, T):
    n = int(input())
    func(n, 4)
    answer[i]=dp[n]

for i in range(0, T):
    print(answer[i])
