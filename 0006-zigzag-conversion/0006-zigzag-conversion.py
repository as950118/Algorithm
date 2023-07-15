class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = numRows # 편의를 위해 n으로
        if n == 1:
            return s

        m = len(s) # s의 길이
        if m == 1:
            return s

        ret = ""
        # 아래 공식에 따라 첫줄과 마지막줄은 (n-1)*2의 스탭만큼 슬라이싱
        ret += s[0::(n-1)*2]

        # 아래 공식에 따라 중간줄은 (n-1-i)*2 와 i*2를 반복해가며 슬라이싱
        for i in range(1, n-1):
            j = i
            flag = True
            while j<m:
                ret += s[j]
                if flag:                    
                    j += ((n-1-i)*2)
                    flag = False
                else:
                    j += i*2
                    flag = True

        # 아래 공식에 따라 첫줄과 마지막줄은 (n-1)*2의 스탭만큼 슬라이싱
        ret += s[(n-1)::(n-1)*2]

        return ret
        '''  
        13579 -> 2
        2468  -> 2

        1 5 9 -> 4
        2468  -> 2,2
        3 7   -> 4

        1  7     13 -> 6
        2 68   1214 -> 4,2
        35 9 11  15 -> 2,4
        4  10    16 -> 6

        1   9  -> 8
        2  810 -> 6,2
        3 7 11 -> 4,4
        46  12 -> 2,6
        5   13 -> 8
        '''