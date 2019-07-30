n = int(input())
arr=list(map(int, input().split()))
dp = [[] for i in range(max(arr)+1)]
for i in range(n):
    dp[arr[i]].append(i)
for q in range(int(input())):
    temp = list(map(int, input().split()))
    if temp[0]==1:
        dp[arr[temp[1]-1]].remove(temp[1]-1)
        arr[temp[1]-1] = temp[2]
        dp[temp[2]].append(temp[1]-1)
    else:
        t = temp[1]
        for i in range(t):
            for j in dp[i]:
                dp[arr[j]].remove(j)
                arr[j] = t
                dp[t].append(j)
for i in range(n):
    print(arr[i], end=" ")
