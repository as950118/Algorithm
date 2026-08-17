class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:        
        n1 = len(str1)
        n2 = len(str2)
        if n1 > n2:
            str1, str2 = str2, str1
            n1 = len(str1)
            n2 = len(str2)
        for i in range(n1, 0, -1):
            split_str1 = set([str1[j:j+i] for j in range(0, n1, i)])
            split_str2 = set([str2[j:j+i] for j in range(0, n2, i)])
            if len(split_str1) == 1 and len(split_str2) == 1 and split_str1 == split_str2:
                return list(split_str1)[0]
        return ""
            


