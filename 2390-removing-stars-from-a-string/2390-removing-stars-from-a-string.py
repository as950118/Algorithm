class Solution:
    def removeStars(self, s: str) -> str:
        ret = []
        for i in s:
            if i == '*':
                ret.pop()
            else:
                ret.append(i)
        return ''.join(ret)