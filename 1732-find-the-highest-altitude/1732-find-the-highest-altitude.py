class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ret = 0
        cur = 0
        for g in gain:
            cur += g
            ret = max(ret, cur)
        return ret