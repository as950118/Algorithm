import sys
sys.setrecursionlimit(1000000000)

def func(arr1, arr2, arr3):
    global ret
    if arr1==arr2:
        return 0
    dp[2] = dp[2] *arr2
    dp[3] = dp[3] *arr3
    if dp[2]%dp[3] == 0:
        dp[2] = dp[2]/dp[3]
        dp[3] = 1
    func(arr1, arr2-1, arr3-1)




N = int(input())
output = [0]*N

for i in range(0, N):
    dp = [1]*4
    arr = [0]*4

    arr[1], arr[2]= input().split()
    arr[1], arr[2] = int(arr[1]), int(arr[2])
    arr[1] = max(arr[1] ,arr[2]-arr[1])
    arr[3] = arr[2]-arr[1]

    if arr[2] == arr[1]:
        dp[2] = 1
    else:
        func(arr[1], arr[2], arr[2]-arr[1])

    output[i] = dp[2]
for i in range(0,N):
    print("%d" %output[i])
