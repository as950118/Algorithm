class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = ""
        for i in range(min(len(word1), len(word2))):
            ret += word1[i] + word2[i]
        if len(word1) < len(word2):
            ret += word2[len(word1):]
        else:
            ret += word1[len(word2):]
        return ret
