import sys, math
from collections import deque
input = lambda:sys.stdin.readline().strip()
INF = sys.maxsize

#Prime Number
prime_num = [1 for i in range(2000)]
prime_num[:2] = [0,0]
def func_prime(n):
    sqrt_n = int(math.sqrt(n))
    for num in range(2,sqrt_n+1):
        if prime_num[i]:
            if not n%num:
                return 0
    return 1
for i in range(3,2000):
    prime_num[i] = func_prime(i)

#Array -> Edge
#모든 소수는 홀수와 짝수의 합이므로
#홀수와 짝수로 나누어서 이분매칭 진행
n = int(input())
arr = list(map(int, input().split()))
arr_even = [i for i in arr if not i%2]
arr_odd = [i for i in arr if i%2]
n_even = len(arr_even)
n_odd = len(arr_odd)
edge = [[]for i in range(n+1)]
for e in range(n_even):
    for o in range(n_odd):
        if prime_num[arr_even[e]+arr_odd[o]]:
            edge[e].append(o)


def bfs(): #그룹A의 Node들의 Level을 매기기 위해서
    que = deque()
    for a in range(1,n_even+1):
        if not groupA[a]: #매칭되어있지않으면 level은 0으로 시작
            dist[a] = 0
            que.append(a)
        else:
            dist[a] = INF
    dist[0] = INF
    while que: #그룹A의 Node들의 Level을 측정
        a = que.popleft()
        if dist[a] < dist[0]:
            for b in edge[a]:
                if dist[groupB[b]] == INF:
                    dist[groupB[b]] = dist[a] + 1
                    que.append(groupB[b])
    return dist[0] != INF

def dfs(a):
    if a:
        for b in edge[a]: #그룹A의 a번째 Node와 연결되어있는 그룹B의 b중에서
            #(매칭되어있지않거나, b에 연결된 a'와 a의 Level이 1차이 나거나), (b에 연결되어있는 a'가 (매칭되어있지않거나, level이 1차이 나면))
            if dist[groupB[b]] == dist[a] + 1 and dfs(groupB[b]):
                groupA[a] = b
                groupB[b] = a
                return 1
        dist[a] = INF
        return 0
    return 1

ret = []
groupA = [0 for i in range(n_even+1)]
groupB = [0 for i in range(n_odd+1)]
dist = [INF for i in range(n_even+1)] #그룹A의 Node들의 Level
while bfs():
    for a in range(1, n_even+1):
        if not groupA[a]: #매칭이 안되어있고
            if dfs(a):
                if not arr[0]%2:
                    ret.append(arr_odd[groupA[1]])
                else:
                    ret.append(arr_even[groupB[1]])
if not ret:
    print(-1)
else:
    for i in ret:
        print(i, end=" ")