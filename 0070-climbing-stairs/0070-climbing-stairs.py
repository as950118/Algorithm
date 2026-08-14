class Solution:
    def climbStairs(self, n: int) -> int:
        visit = {}
        def climb(cur):
            if cur in visit:
                return visit[cur]
            if cur > n:
                visit[cur] = 0
                return 0
            if cur == n:
                visit[cur] = 1
                return 1
            a = climb(cur+1)
            b = climb(cur+2)
            visit[cur+1] = a
            visit[cur+2] = b
            return a + b
        return climb(1) + climb(2)
