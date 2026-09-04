class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)
        ret = 0
        for i in range(n):
            path = [i]
            if i in visited:
                continue
            while path:
                cur = path.pop()
                if cur in visited:
                    continue
                visited.add(cur)
                for i in range(n):
                    if cur == i:
                        continue
                    if isConnected[cur][i]:
                        path.append(i)
            ret += 1
        return ret
