'''
1. 글자의 길이가 같아야함
2. 글자별로 존재하는 갯수들의 목록이 동일해야함.
'''
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dic1 = {}
        dic2 = {}
        for word in word1:
            if word in dic1:
                dic1[word] +=1
            else:
                dic1[word] = 1

        for word in word2:
            if word in dic2:
                dic2[word] +=1
            else:
                dic2[word] = 1

        keys1 = list(dic1.keys())
        keys2 = list(dic2.keys())
        values1 = list(dic1.values())
        values2 = list(dic2.values())
        keys1.sort()
        keys2.sort()
        values1.sort()
        values2.sort()

        return keys1 == keys2 and values1 == values2