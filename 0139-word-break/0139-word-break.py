from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [[None] * n for i in range(n)]
        def func(k):
            if k == n:
                return True
            if dp[k][n-1] != None:
                return dp[k][n-1]
            for i in range(k, n):
                if s[k:i+1] in word_set:
                    ret = func(i+1)
                    if ret:
                        dp[k][i] = True
                        return dp[k][i]            
                else:
                    dp[k][i] = False
            if dp[0][k] == None:
                dp[0][k] = False
            return dp[0][k]
        return func(0)

