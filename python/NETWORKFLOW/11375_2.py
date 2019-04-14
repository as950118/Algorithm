import sys
input = lambda:sys.stdin.readline().strip()

def dfs(a):
    visit[a] = 1
    for b in graph[a]:
        next_a = groupB[b]
        if not next_a or not visit[next_a] and dfs(next_a):
            groupA[a] = b
            groupB[b] = a
            return 1
    return 0

n, m = map(int, input().split())
graph = [[]] #직원 - 일 관계
groupA = [0 for i in range(n+1)]
groupB = [0 for i in range(m+1)]
for i in range(n):
    graph.append(list(map(int, input().split()))[1:])
ret = 0
for i in range(1,n+1):
    if not groupA[i]: #아직 매칭되지 않았다면
        visit = [0 for i in range(n+1)]
        ret += dfs(i)
print(ret)
