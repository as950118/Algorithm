class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        for i in range(n, 0, -1):
            for j in range(0, n-i+1):
                if s[j:j+i] == s[j:j+i][::-1]:
                    return s[j:j+i]