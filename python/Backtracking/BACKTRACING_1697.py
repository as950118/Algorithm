n,k = map(int, input().split())
visited = [0 for i in range(max(n,k)*2 + 1)]#리스트의 크기는 n,k중 큰 값 * 2 + 1
def func():
    bfs = []
    bfs.append(n)
    while bfs:
        cur = bfs.pop(0)
        if cur == k:
            return visited[cur]
        if cur>-1: #음의 값은 고려할 필요 없음
            if cur<k: #도착점보다 작을 경우는 모두 고려해야하자만
                if not visited[cur+1]:
                    visited[cur+1] = visited[cur] + 1
                    bfs.append(cur+1)

                if not visited[cur*2]:
                    visited[cur*2] = visited[cur] + 1
                    bfs.append(cur*2)

                if not visited[cur-1]:
                    visited[cur-1] = visited[cur] + 1
                    bfs.append(cur-1)
            else: #도착점보다 클 경우는 감소하는 값만 고려하면됨
                if not visited[cur-1]:
                    visited[cur-1] = visited[cur] + 1
                    bfs.append(cur-1)

print(func())
