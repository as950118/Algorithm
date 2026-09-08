class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0 for i in range(n)] for j in range(m)]
        cache[0][0] = 1
        for i in range(n):
            cache[0][i] = 1
        for j in range(m):
            cache[j][0] = 1
        for j in range(1, m):
            for i in range(1, n):
                cache[j][i] += cache[j-1][i]
                cache[j][i] += cache[j][i-1]
        return cache[m-1][n-1]