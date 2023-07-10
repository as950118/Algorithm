class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        sets = set()
        index = {}

        start = 0
        end = 0
        max_len=0

        n = len(s)
        for i in range(n):
            cur = s[i]
            if cur in sets:
                index_cur = index[cur]
                start = max(start, index_cur+1)
                end = i
                index[cur] = i
                sets = set(s[start:end+1])
            else:
                sets.add(cur)
                index[cur] = i
                end = i
            max_len = max(max_len, end-start)
        return max_len+1