import sys
import math
#import thread
sys.setrecursionlimit(1000000000)
from collections import deque
'''
n을 k개로 만들어야하므로
그 경우의 수는 nC0 + nC1 + nC2 .. nC(k-1) 이다.
그냥 nCk가 아니냐고 생각할 수도 있지만
0도 포함되므로, nC0부터 nCk까지이디.
그러므로 1 + n + n*n-1/2 + n*n-1*n-2/2*3..를 계산하면된다.
'''
n, k = map(int, input().split())
dp_a = [0]*(k+1)
dp_b = [0]*(k+1)
dp = [0]*(k+1)
dp[1] = 1
dp_a[1] = 1
dp_b[1] = 1
sum = 1
for i in range(2, k+1):
    #dp_a[i] = dp_a[i-1] * (n+i-1)
    #dp_b[i] = dp_b[i-1] * i-1
    dp[i] = (dp[i-1]*(n+i-1))/i-1
    #sum = sum + (dp_a[i] // dp_b[i])
print(int(sum)%1000000000)
print(dp[k])
