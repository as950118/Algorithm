import sys

n,k = map(int, input().split())
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(input())

ret = 0

for i in range(n):
    temp = k//arr[n-i-1]
    k %= arr[n-i-1]
    ret += temp
    if k==0:
        break
print(ret)
