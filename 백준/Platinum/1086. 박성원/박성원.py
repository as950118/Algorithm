from math import factorial
from math import gcd

import sys
input = lambda:sys.stdin.readline().strip()
N=int(input())
num=[0]*N          # 숫자들을 저장하는 리스트
num_len=[0]*N      # 각 숫자들의 길이를 저장하는 리스트
for i in range(N): # num과 num_len을 채우는 과정
    t=input()
    num[i]=int(t)
    num_len[i]=len(t)
k=int(input())
full=2**N-1
# bit에 의해 생성되는 전체 경우의 수 ex) 111111111
each_bit=[2**i for i in range(N)]
# 1 10 100 1000 10000 100000 각각의 비트를 선택하기 위해 리스트에 저장(2비트)
plen=sum(num_len)
rm=[[0]*plen for i in range(N)]
# 주어지는 집합에서 주어지는 숫자들이 위치에 따라서 달라지는 나머지 수
# ex) 423라는 수가 주어진다면 423000 42300 4230 423에 대한 각각의 나머지를 저장
for i in range(N):
    mx=plen-num_len[i]
    for j in range(mx+1):
        rm[i][j]=num[i]*10**(mx-j)%k
dp=[[-1]*(full+1) for _ in range(100)]

def solve(length, bit, remain):
    if bit==full:
        return remain==0
    if dp[remain][bit]!=-1:
        return dp[remain][bit]
    dp[remain][bit]=0
    for n in range(N):
        if not bit & each_bit[n]:
            dp[remain][bit]+=solve(length+num_len[n], bit | each_bit[n],(remain+rm[n][length])%k)
    return dp[remain][bit]

result=solve(0,0,0)
g=gcd(result,factorial(N))
# print(result, g)
if result==0:
    print("0/1")
else:
    print("%d/%d"%(result//g, factorial(N)//g))