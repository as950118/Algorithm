class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min(map(len, strs))
        ret = ""
        for i in range(n):
            if len(set(map(lambda x:x[i], strs))) == 1:
                ret += strs[0][i]
            else:
                break
        return ret