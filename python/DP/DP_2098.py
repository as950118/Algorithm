import sys

n = int(sys.stdin.readline())
numsquare = 1<<n
start = 0
visitedAll = (numsquare) - 1


arr = [[] for i in range(n)]


for i in range(n):
    for j in map(int,sys.stdin.readline().split()):
        if j == 0:
            arr[i].append(None)
        else :
            arr[i].append(j)

dp = [[ -1]*(numsquare) for i in range(n)]
for i in range(numsquare):
    if i == 1:
        dp[0][i] = 0
    else:
        dp[0][i] = None

def func(cur, prv):
    if dp[cur][prv] == -1:
        compare = []
        prvprv = prv & (~(1<<cur))
        for i in range(prvprv.bit_length()):
            if (prvprv >> i) & 1:
                before = i
            else:
                continue
            if func(before, prvprv)!=None and arr[before][cur]!=None:
                compare.append(func(before, prvprv)+arr[before][cur])
        if compare:
            dp[cur][prv] = min(compare)
        else:
            dp[cur][prv] = None
        return dp[cur][prv]
    else:
        return dp[cur][prv]

endPoint = list()
for last in range(1,n) :
    if func(last, visitedAll)!=None and arr[last][start]!=None:
        endPoint.append(func(last, visitedAll)+arr[last][start])
print(min(endPoint))
