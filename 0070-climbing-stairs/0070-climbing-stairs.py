class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {0: 1, 1: 1}
        # def climb(cur):
        #     if cur in memo:
        #         return memo[cur]
        #     memo[cur] = climb(cur-1) + climb(cur-2)
        #     return memo[cur]
        # return climb(n)
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b        
        return b
