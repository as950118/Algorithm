import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
arr = str(input())
ret = 0
for i in range(n):
    if int(arr[i])%2==0:
        ret += (i+1)
print(ret)
