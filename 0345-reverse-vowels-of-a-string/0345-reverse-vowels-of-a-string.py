class Solution:
    def reverseVowels(self, s: str) -> str:
        aeiou = [i for i in "aeiouAEIOU"]
        aeiou_in_s = []
        for e in s:
            if e in aeiou:
                aeiou_in_s.append(e)
        ret = ''
        for e in s:
            if e in aeiou:
                ret += aeiou_in_s.pop()
            else:
                ret += e
        return ret
