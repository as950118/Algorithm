class Solution:
    def isDigit(self, c:str) -> bool:
        return c in [str(i) for i in range(10)]

    def toDigit(self, c:str) -> int:
        return int(c)
        
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        flag = 1 # 음=0 양=1
        if not s:
            return 0
        if s[0] == "-":
            flag = 0
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        splited_s = ""
        for c in s:
            if self.isDigit(c):
                splited_s += c
            else:
                break
        try:
            if flag:
                ret = int(splited_s)
            else:
                ret = -int(splited_s)
        except Exception as e:
            ret = 0
        if ret > 2**31 - 1:
            ret = 2**31 - 1
        if ret < -2**31:
            ret = -2**31
        return ret