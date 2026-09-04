class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        ret = 0

        def dfs(cur):
            visited.add(cur)

            for neighbor in range(n):
                if isConnected[cur][neighbor] and neighbor not in visited:
                    dfs(neighbor)

        for i in range(n):
            if i not in visited:
                dfs(i)
                ret += 1

        return ret