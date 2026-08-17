from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [None] * n
        def func(k):
            if k == n:
                return True
            if dp[k] != None:
                return dp[k]
            for i in range(k, n):
                if s[k:i+1] in word_set:
                    ret = func(i+1)
                    if ret:
                        dp[k] = True
                        return dp[k]
                    else:
                        dp[k] = False
                else:
                    dp[k] = False
            if dp[0] == None:
                dp[0] = False
            return dp[0]
        return func(0)

