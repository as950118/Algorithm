class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        memo = {}

        def func(k):
            if k == n:
                return True
            if k in memo:
                return memo[k]
            for j in range(k, n):
                if s[k:j+1] in word_set and func(j+1):
                    memo[k] = True
                    return True
            memo[k] = False
            return False

        return func(0)