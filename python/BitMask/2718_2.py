import sys
sys.setrecursionlimit(10**6)
input = lambda:sys.stdin.readline().strip()

dp = [[-1 for i in range(1<<4)] for ii in range(10**2)]

bit_list = [0, (1<<0)+(1<<1), (1<<1)+(1<<2), (1<<0)+(1<<3), (1<<2)+(1<<3)] #0000, 0011, 0110, 1001, 1100

def bit_0000(cur):
    return func(cur-2, bit_list[0]) + func(cur-1, bit_list[0]) + func(cur-1, bit_list[1]) + func(cur-1, bit_list[3]) + func(cur-1, bit_list[4])
def bit_0011(cur):
    return func(cur-1, bit_list[0]) + func(cur-1, bit_list[4])
def bit_0110(cur):
    return func(cur-1, bit_list[3])
def bit_1001(cur):
    return func(cur-1, bit_list[0]) + func(cur-1, bit_list[2])
def bit_1100(cur):
    return func(cur-1, bit_list[0]) + func(cur-1, bit_list[1])

#cur는 현재위치, bit는 놓여진 위치를 bitmasking한 값
def func(cur, bit):
    if cur < 0:
        return 0
    if cur == 0:
        return bit==0
    if dp[cur][bit] != -1:
        return dp[cur][bit]

    if bit == bit_list[0]: #0000
        dp[cur][bit] = bit_0000(cur)
    if bit == bit_list[1]: #0011
        dp[cur][bit] = bit_0011(cur)
    if bit == bit_list[2]: #0110
        dp[cur][bit] = bit_0110(cur)
    if bit == bit_list[3]: #1001
        dp[cur][bit] = bit_1001(cur)
    if bit == bit_list[4]: #1100
        dp[cur][bit] = bit_1100(cur)

    return dp[cur][bit]

for t in range(int(input())): #반복할 횟수
    n = int(input())
    print(func(n,0))
