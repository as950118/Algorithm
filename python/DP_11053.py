import sys
sys.setrecursionlimit(1000000000)

dp = [0]*1000000
arr = [0]*1000000
arr2 = [0]*1000000
ret = 0

def func(n, i):
    global ret
    if n<i:
        return 0
    if dp[i-1]<arr2[i]:
        dp[i] = arr2[i]
        ret+=1
    else:
        dp[i] = dp[i-1]

    func(n, i+1)


N = int(input())

arr = input().split()

for i in range(0, N):
    arr2[i+1] = int(arr[i])


func(N, 1)
print(ret)
